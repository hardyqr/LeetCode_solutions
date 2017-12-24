# Freddy/Fangyu@BNU
# 12/20/2016

class Solution(object):
    def plusOne(self, digits):
        s=''
        for x in digits:
            s+=str(x)
        aws=[]
        for y in str(int(s)+1):
            aws.append(int(y))
        return aws
