# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        return self.dfs(root)[1]
    
    def dfs(self, root):

        if root is None:
            return 0, 0
        height_l, diameter_l = self.dfs(root.left)
        height_r, diameter_r = self.dfs(root.right)

        diameter = max(height_l + height_r, diameter_l, diameter_r)
        height = 1 + max(height_l, height_r)

        return (height, diameter)


