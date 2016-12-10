# Fangyu/Freddy
# 12/11/2016

# recursion
def add(n):
    if n > 0:
        return n + add(n - 1)

def addDigit(x):
    r=0
    for i in str(x):
        r+=int(i)
    if len(str(r))==1:
        # print(r)
        return r
    else:
        return addDigit(r)

# 为什么在solution内部写addDigits递归会报错？
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        r=0
        for i in str(num):r+=int(i)
        if len(str(r))==1:
            # print(r)
            return r
        else:
            return addDigit(r)
    # addDigits(object,1552)
