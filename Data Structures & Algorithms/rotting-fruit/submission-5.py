class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        Foundfresh = False
        Foundrotten = False
        q = deque()
        visited = set()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append([i,j])
                    visited.add((i,j))
                    Foundrotten = True
                if grid[i][j] == 1:
                    Foundfresh = True

        if Foundfresh is False:
            return 0
            

        Otherrotten = False
        time = -1

        while q:
            
            time+=1
            for i in range(len(q)):
                row, col = q.popleft()
                grid[row][col] = 2
                self.Futurerotten(row+1, col, grid, visited, q)
                self.Futurerotten(row-1, col, grid, visited, q)
                self.Futurerotten(row, col+1, grid, visited, q)
                self.Futurerotten(row, col-1, grid, visited, q)

                if len(q)>0:
                    Otherrotten = True

        if Otherrotten == False:
            return -1
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return -1

        return time

    def Futurerotten(self, row, col, grid, visited, q):

        n_r = len(grid)
        n_c = len(grid[0])
        if row in range(n_r) and col in range(n_c) and grid[row][col]==1 and (row, col) not in visited:
            q.append([row, col])
            visited.add((row, col))
    


        



        