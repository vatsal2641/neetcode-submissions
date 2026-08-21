class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hash_map = {}

        # LRU ←→ ... ←→ MRU
        self.head = None
        self.tail = None

    def _remove(self, node):
        """Remove node from the doubly linked list."""
        if node == self.head:
            self.head = node.next

        if node == self.tail:
            self.tail = node.prev

        if node.prev:
            node.prev.next = node.next

        if node.next:
            node.next.prev = node.prev

        node.prev = None
        node.next = None

    def _add_to_tail(self, node):
        """Add node as the most recently used node."""
        node.prev = self.tail
        node.next = None

        if self.tail:
            self.tail.next = node
        else:
            # Empty list
            self.head = node

        self.tail = node

    def _move_to_tail(self, node):
        """Mark an existing node as most recently used."""
        if node == self.tail:
            return

        self._remove(node)
        self._add_to_tail(node)

    def get(self, key: int) -> int:
        if key not in self.hash_map:
            return -1

        node = self.hash_map[key]

        # Access makes it most recently used
        self._move_to_tail(node)

        return node.val

    def put(self, key: int, value: int) -> None:

        # Case 1: key already exists
        if key in self.hash_map:
            node = self.hash_map[key]
            node.val = value

            # Update makes it most recently used
            self._move_to_tail(node)
            return

        # Case 2: inserting a new key
        new_node = Node(key, value)
        self.hash_map[key] = new_node
        self._add_to_tail(new_node)

        # Cache exceeded capacity
        if len(self.hash_map) > self.capacity:
            lru = self.head
            self._remove(lru)
            del self.hash_map[lru.key]