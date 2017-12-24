# Freddy/Fangyu@BNU
# 12/20/2016

def agent(num):
    if num==1:
        return True
    elif num%2==0 and num!=0:
        if num/2==1:
            return True
        else:
            num/=2
            return agent(num)
    else:
        return False
class Solution(object):
    def isPowerOfTwo(self, n):
        return agent(n)
