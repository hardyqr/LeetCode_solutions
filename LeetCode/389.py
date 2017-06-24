# Freddy/Fangyu@BNU
# 12/18/2016

class Solution(object):
    def findTheDifference(self, s, t):

        for i in t:
            if s.count(i)!=t.count(i):
                return i
        
