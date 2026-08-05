from collections import Counter
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            lis = board[i][:]
            check = Counter(lis)
            del check["."]
            for val in check.values():
                if val>1:
                    return False

        for i in range(9):
            lis = []
            for j in range(9):
                lis.append(board[j][i])
            check = Counter(lis)
            del check["."]
            for val in check.values():
                if val>1:
                    return False

        for i in range(0, 9, 3):
            for j in range(0,9,3):
                lis=[]
                for k in range(3):
                    for l in range(3):
                        lis.append(board[i+k][j+l])
                check = Counter(lis)
                del check["."]
                for val in check.values():
                    if val>1:
                        return False
        
        return True
        
