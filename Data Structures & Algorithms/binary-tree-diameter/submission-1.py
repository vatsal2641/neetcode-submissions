# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


FINAL_D = 0
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return 0

        diameter = self.maxdepth(root.left) + self.maxdepth(root.right)


        diameter_l = self.diameterOfBinaryTree(root.left)
        diameter_r = self.diameterOfBinaryTree(root.right)

        
        return max(diameter, diameter_l, diameter_r)

    def maxdepth(self, root):
        if root is None:
            return 0
        
        return 1 + max(self.maxdepth(root.left), self.maxdepth(root.right))
