# Freddy/Fangyu@BNU
# 12/19/2016

class Solution(object):
    def findNthDigit(self, n):
        num=1
        digit=9
        while n>digit*num:
            n=n-digit*num
            digit*=10
            num+=1
        print(n,digit,num)
p=Solution()
p.findNthDigit(3)
p.findNthDigit(11)
p.findNthDigit(111)
