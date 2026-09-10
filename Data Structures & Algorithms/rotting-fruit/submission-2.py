class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        contains_rotten = False
        contains_fruit = False

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==2:
                    q.append([i,j])
                    visited.add((i,j))
                    contains_rotten = True
                if grid[i][j]==1:
                    contains_fruit = True
        
        if not contains_rotten and not contains_fruit:
            return 0 
            
        time = -1

        while q:
            
            time+=1
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = 2   #You are rotten now
                self.futurerotten(r+1, c, visited, q, grid)
                self.futurerotten(r-1, c, visited, q, grid)
                self.futurerotten(r, c+1, visited, q, grid)
                self.futurerotten(r, c-1, visited, q, grid)


        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    return -1   
                

        return time
            
    def futurerotten(self,r,c,visited,q,grid):
        n_r = len(grid)
        n_c = len(grid[0])
        if r<0 or r==n_r or c<0 or c==n_c or (r,c) in visited or grid[r][c]==2 or grid[r][c] == 0:
            return 
        
        q.append([r,c])
        visited.add((r,c))
    
