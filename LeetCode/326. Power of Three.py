# Freddy/Fangyu@BNU
# 12/20/2016

def agent(num):
    if num==1:
        return True
    elif num%3==0 and num!=0 and num!=2:
        if num/3==1:
            return True
        else:
            num/=3
            return agent(num)
    else:
        return False

class Solution(object):
    def isPowerOfThree(self, n):
        return agent(n)
