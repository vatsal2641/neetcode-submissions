# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_val):
            if not node:
                return 0

            if node.val >= max_val:
                good_node = 1 
                curr_max = node.val
            
            else:
                good_node = 0
                curr_max = max_val
            
            return good_node + dfs(node.left, curr_max) + dfs(node.right, curr_max)
        
        return dfs(root, root.val)
            
        