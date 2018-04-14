# April 13, 2018 @BH

class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        steps = [(1,0),(-1,0),(0,1),(0,-1)]
        m = len(grid)
        n = len(grid[0])
        def DFS(grid, x,y,m,n):
            if (x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == 0): # boundaries reached or no island
                return 0
            # else, grid[x][y] = 1
            res = 1
            grid[x][y] = 0
            for i,j in steps:
                res += DFS(grid,x+i,y+j,m,n)
            return res
        res = 0
        for i in range(m):
            for j in range(n):
                if (grid[i][j] == 1):
                    res = max(res, DFS(grid,i,j,m,n))
        return res
            
        
