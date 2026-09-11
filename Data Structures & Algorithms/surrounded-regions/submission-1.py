class Solution:
    def solve(self, board: List[List[str]]) -> None:
        R = len(board)
        C = len(board[0])
        visited = set()
        convert_locs = []
        region_coords= []
        for i in range(R):
            for j in range(C):
                if board[i][j] == "O" and (i,j) not in visited:
                    region_coords = self.BFS(i,j,board,visited)  #BFS true then convert all the ele X but we need to store them somewhere. 
    
                    convert_locs+=region_coords


        for i,j in convert_locs:
            board[i][j] = "X"
        
    def BFS(self, r,c, board, visited):
        region_values = []
        q = deque()
        q.append([r,c])
        visited.add((r,c))
        boundary_exists= False
        if r not in [0,len(board)-1] and c not in [0, len(board[0])-1]:
            region_values.append([r,c])
        else: 
            boundary_exists= True
        
        while q:
            
            row, col = q.popleft()
            
            if self.see_neighbor(row+1, col, region_values, board, visited,q):
                boundary_exists = True
            if self.see_neighbor(row-1, col, region_values, board, visited, q):
                boundary_exists = True
            if self.see_neighbor(row, col+1, region_values, board, visited, q):
                boundary_exists = True
            if self.see_neighbor(row, col-1, region_values, board, visited, q):
                boundary_exists = True
               
        if boundary_exists is True:
            return []

        return region_values
            
    
    def see_neighbor(self, r, c, region_values, board, visited, q):
        R = len(board)
        C = len(board[0])
    
        if (r in range(R)) and (c in range(C)) and (board[r][c] == "O") and ((r,c) not in visited):
            visited.add((r,c))
            q.append([r,c])
          
            if r in [0, R-1] or c in [0, C-1]:
                return True
    
            region_values.append([r,c])
            
            
    


        



            