# Freddy/Fangyu
# 12/15/2016

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        rows=[]
        if numRows==0:return rows
        previous=[1]
        rows.append(previous)
        if numRows==1:return rows
        for m in range(1,numRows):
            current=[]
            current.append(1)
            for i in range(0,len(previous)-1):
                current.append(previous[i]+previous[i+1])
            current.append(1)
            previous=current
            rows.append(previous)
        # print(rows)
        return rows
    # generate(object,0)
    # generate(object,3)
    # generate(object,5)
