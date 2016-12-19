# Freddy/Fangyu@BNU
# 12/19/2016

def check(num):
    if num%4 == 0:
        if num/4 != 1:
            num=int(num/4)
            print(num)
            check(num)
        else:
            return True
    else:
        return False

class Solution(object):
    def isPowerOfFour(self, num):
        if num==0:
            return True
        else:
            return check(num)

a=Solution()
a.isPowerOfFour(16)
#a.isPowerOfFour(0)
