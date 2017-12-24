# Freddy/Fangyu
# 12/11/2016

class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n%4!=0

'''
n=1 win
n=2 win
n=3 win
n=4 lose
n=5 win
n=6 win
n=7 win
n=8 lose
n=9 win
...
lose when 4 is a factor of n
'''
