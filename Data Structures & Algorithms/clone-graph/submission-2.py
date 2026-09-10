"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return node

        oldtonew={node: Node(node.val)}
        q = deque()
        q.append(node)
        while q:
            cur_node = q.popleft()
            for neighbor in cur_node.neighbors:
                if neighbor not in oldtonew:
                    oldtonew[neighbor] = Node(neighbor.val)
                    q.append(neighbor)

                oldtonew[cur_node].neighbors.append(oldtonew[neighbor])

        return oldtonew[node]