class Solution:
    #IN COPY
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        r = len(grid)
        c = len(grid[0])
        visited = set()
        q = deque()


        #lets start from treasure chest
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 0:
                    q.append([i,j])
                    visited.add((i,j))
            

        dist = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()

                grid[r][c]=dist

                self.addland(r+1, c, grid, visited, q)
                self.addland(r-1, c, grid, visited, q)
                self.addland(r, c+1, grid, visited, q)
                self.addland(r, c-1, grid, visited, q)
            
            dist+=1  #All the gates over now dist1 will come then dist2 will come and so on..
        
    def addland(self, r,c,grid,visited,q):
        
        n_r = len(grid)
        n_c = len(grid[0])

        if r<0 or (r>=n_r) or c<0 or (c>=n_c) or ((r,c) in visited) or (grid[r][c] == -1) : 
            return 
        
        q.append([r,c])
        visited.add((r,c))

                


