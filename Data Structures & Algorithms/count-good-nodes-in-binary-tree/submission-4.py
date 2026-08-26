# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Optimized solution by claude to see later
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_val):
            if not node:
                return 0
            
            # Node is good if its value is >= max value on the path
            is_good = 1 if node.val >= max_val else 0
            
            # Update the path maximum for child calls
            current_max = max(max_val, node.val)
            
            # Aggregate counts from left and right subtrees
            return is_good + dfs(node.left, current_max) + dfs(node.right, current_max)

        return dfs(root, root.val)
        