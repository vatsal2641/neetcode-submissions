class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])

        visit = set()

        islands = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and (r,c) not in visit:
                    self.BFS(grid, visit, r, c)
                    islands+=1
        
        return islands

    def BFS(self, grid, visit, r, c):

        visit.add((r,c))
        q= deque()
        q.append((r,c))

        directions = [[1,0], [-1,0], [0,-1], [0,1]]
        while q:
            row, col = q.popleft()

            for dr, dc in directions:
                if ((row+dr) in range(len(grid))) and ((col+dc) in range(len(grid[0])) and (grid[row+dr][col+dc] == "1") and ((row+dr, col+dc) not in visit)):
                     

                    q.append((row+dr, col+dc))

                    visit.add((row+dr, col+dc))