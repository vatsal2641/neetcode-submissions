# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        ans = []

        level_order = self.levelorder(root)

        if len(level_order)==0:
            return level_order
        
        for arr in level_order:
            ans.append(arr[-1])

        return ans

    def levelorder(self, root):
        if root is None:
            return []

        ans_level = []

        q = deque()

        q.append(root)

        while q:
            curr_level = []
            for i in range(len(q)):
                temp = q.popleft()
                curr_level.append(temp.val)
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
            ans_level.append(curr_level)
        return ans_level
