"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


#Applying BFS

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return node
        # clone_node = Node(node.val)

        # Map original node -> cloned node
        old_to_new = {node: Node(node.val)}

        q = deque()
        q.append(node)
        while q:
            curr_node= q.popleft()
            for neighbor in curr_node.neighbors:

                if neighbor not in old_to_new:
                    old_to_new[neighbor] = Node(neighbor.val)
                    q.append(neighbor)
                
                old_to_new[curr_node].neighbors.append(
                    old_to_new[neighbor]
                )

        return old_to_new[node]
                




        