class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        curr_area = 0
        r = len(grid)
        c = len(grid[0])
        visited = set()

        for i in range(r):
            for j in range(c):
                if (i,j) not in visited and grid[i][j]==1:
                    curr_area = self.BFS(grid, visited, i,j)
                    if curr_area>max_area:
                        max_area = curr_area

        return max_area
    
    def BFS(self, grid, visited, r,c):
        curr_area = 1
        q = deque()
        q.append((r,c))
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        visited.add((r,c))
        while q:
            row, col = q.popleft()
            for dr, dc in directions:
                
                n_r, n_c = row+dr, col+dc

                if (n_r in range(len(grid))) and (n_c in range(len(grid[0]))) and (grid[n_r][n_c] == 1) and ((n_r, n_c) not in visited):
                    q.append((n_r, n_c))
                    visited.add((n_r, n_c))
                    curr_area += 1



        return curr_area