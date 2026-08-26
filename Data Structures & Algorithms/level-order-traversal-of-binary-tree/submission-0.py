# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #queue ds will be used here. 

        if root is None:
            return []
            
        q = deque()

        ans = []

        temp = None

        q.append(root)

        while q:
            
            curr_ans = []

            for i in range(len(q)):

                temp = q.popleft()
                curr_ans.append(temp.val)
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)

            ans.append(curr_ans)
        
        return ans

            


            


