# Fnagyu
# 12/4/2016


class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        h=len(grid)
        w=len(grid[0])
        count=0
        a=0
        while a<h-1:
            b=0
            while b<w-1:
                if grid[a][b]==1 and grid[a+1][b]==1:
                    count+=1
                if grid[a][b]==1 and grid[a][b+1]==1:
                    count+=1
                b+=1
            a+=1
        b=0
        while b<w-1:
            if grid[h-1][b]==1 and grid[h-1][b+1]==1:
                count+=1
            b+=1
        a=0
        while a<h-1:
            if grid[a][w-1]==1 and grid[a+1][w-1]==1:
                count+=1
            a+=1


        aws=0
        for line in grid:
            for i in line:
                if i==1:aws+=1
        result=aws*4-count*2
        # print(aws,count,result)
        return result

    # islandPerimeter(object,[[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]])
    # islandPerimeter(object,[[1],[1]])
