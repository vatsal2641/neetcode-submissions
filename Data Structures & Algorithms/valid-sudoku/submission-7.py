class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        dict_r = defaultdict(set)
        dict_c = defaultdict(set)
        dict_block = defaultdict(set)
        for i in range(9):
            for j in range(9):
                ele = board[i][j]
                if ele==".":
                    continue
                if (ele in dict_r[i]) or (ele in dict_c[j]) or (ele in dict_block[(i//3, j//3)]) : 
                    return False
                
                else:
                    dict_r[i].add(ele)
                    dict_c[j].add(ele)
                    dict_block[(i//3, j//3)].add(ele)
        
        return True
