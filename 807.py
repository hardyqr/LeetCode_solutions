# April 11, 2018 @DP

import numpy as np
class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        size = len(grid)
        new_grid = np.zeros((size,size))
        gridT = np.array(grid).T
        for i in range(size):
            for j in range(size):
                new_grid[i][j] = min( max(grid[i]), max(gridT[j]))
        return int(new_grid.sum() - gridT.sum())
