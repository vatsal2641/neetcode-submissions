class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows= len(grid)
        cols= len(grid[0])
        visited = set()
        islands = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i,j) not in visited:
                    self.BFS(i, j, visited, grid)
                    islands+=1

        return islands


    def BFS(self, r, c, visited, grid):
        n_r = len(grid)
        n_c = len(grid[0])
        q = deque()
        q.append([r,c])

        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        while q:
            
            row, col = q.popleft()
            for dr, dc in directions:
                rows = row+dr
                cols = col+dc
                if (rows in range(n_r)) and (cols in range(n_c)) and grid[rows][cols] == "1" and (rows, cols) not in visited:
                 
                    q.append([rows, cols])
                    visited.add((rows, cols))
 

