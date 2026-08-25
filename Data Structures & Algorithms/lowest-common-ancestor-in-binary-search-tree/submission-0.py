# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        path_p = []
        path_q = []

        if not self.findPath(root, path_p, p.val) or not self.findPath(root, path_q, q.val):  #What if the element is not present only. 
            return None
        
        else:
            i=0
            while i<len(path_p) and i<len(path_q):
                if path_p[i].val == path_q[i].val:
                    i+=1
                    continue


                break
                
        
            return path_p[i-1]


    
    def findPath(self, root, path, x):
        if root is None:
            return False
        
        path.append(root)

        if root.val == x:
            return True

        if self.findPath(root.left, path, x) or self.findPath(root.right, path, x):
            return True
        
        path.pop()   # The element is neither x nor any of the dexscendent node of x has the path. 

        return False