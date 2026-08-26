# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        st = []
        ans = [1]
        return self.Node(root, ans, st)
    
    # I used stack to compare the elements in O(1) time. 
    #made another function so that I can keep a track of stack and the answer. 
    #I chose answer to be list because the list is mutable and retains the values when called into another functions. 

    
    def Node(self, root, count, stack):
        if len(stack) == 0:
            stack.append(root.val)
        
        elif stack[-1]<=root.val:
            stack.append(root.val)
            count[0]+=1


        if root.left:
            self.Node(root.left, count, stack)

            if len(stack) and stack[-1]==root.left.val:
                stack.pop()

        if root.right:
            self.Node(root.right, count, stack)
            if len(stack) and stack[-1]==root.right.val:
                stack.pop()

        return count[0]


        
