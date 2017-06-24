# Freddy/Fangyu@BNU
# 12/25/2016

class Solution(object):
    '''
    1:1
    2:2
    3:3
    4:5
    5:8
    ...
    '''
    def climbStairs(self, n):
        if n==1:return 1
        x=1
        y=2
        for i in xrange(3,n+1):
           mid=y
           y=x+y
           x=mid
        print(y)
        return y
p=Solution()
p.climbStairs(3)
p.climbStairs(5)
p.climbStairs(2)
p.climbStairs(1)
