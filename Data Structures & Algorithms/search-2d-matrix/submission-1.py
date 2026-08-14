class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        if target < matrix[0][0]:
            return False

        elif target > matrix[-1][-1]:
            return False

        for i in range(len(matrix)):
            if i!=0 and target<matrix[i][0]:
                return False
            if target>matrix[i][-1]:
                continue
            else:
                l = 0
                h = len(matrix[i]) - 1
                while l<=h:
                    mid = (l+h)//2
                    if target == matrix[i][mid]:
                        return True
                    elif target < matrix[i][mid]:
                        h = mid-1
                    else:
                        l = mid+1

        return False