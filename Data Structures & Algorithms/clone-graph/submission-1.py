"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node

        oldtonew = {node: Node(node.val)}
        q = deque()
        q.append(node)

        while q:
            curr_node = q.popleft()
            for neighbor in curr_node.neighbors:
                if neighbor not in oldtonew:     #means that it is not visited
                    oldtonew[neighbor] = Node(neighbor.val)
                    q.append(neighbor)

                oldtonew[curr_node].neighbors.append(oldtonew[neighbor])


        return oldtonew[node]
