class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        atl = set()
        pac = set()

        R = len(heights)
        C = len(heights[0])

        for c in range(C):
            self.dfs(0, c, heights, pac, heights[0][c])
            self.dfs(R-1, c, heights, atl, heights[R-1][c])

        for r in range(R):
            self.dfs(r, 0, heights, pac, heights[r][0])
            self.dfs(r, C-1, heights, atl, heights[r][C-1])

        res = []

        for i in range(R):
            for j in range(C):
                if (i,j) in atl and (i,j) in pac:
                    res.append([i,j])

        return res
    

    def dfs(self, r, c, heights, visited, prevHeight):
        R = len(heights)
        C = len(heights[0])
        if r==R or c ==C or r<0 or c<0 or (r,c) in visited or heights[r][c]<prevHeight:
            return
        #or we go dfs to adjacent locations after adding the cell to visited. 
        visited.add((r,c))

        self.dfs(r+1, c, heights, visited, heights[r][c])
        self.dfs(r, c+1, heights, visited, heights[r][c])
        self.dfs(r-1, c, heights, visited, heights[r][c])
        self.dfs(r, c-1, heights, visited, heights[r][c])

        
