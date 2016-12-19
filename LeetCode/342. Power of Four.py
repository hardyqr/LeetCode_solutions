# Freddy/Fangyu@BNU
# 12/19/2016


def check(num):
    if (num%4 == 0 and num!=0) or num==1 :
        if int(num/4)==1 or num==1:
            return True
        else:
            t=int(num/4)
            return check(t)
    else:
        return False

class Solution(object):
    def isPowerOfFour(self, num):
        return check(num)


a=Solution()
a.isPowerOfFour(16)
#a.isPowerOfFour(0)
