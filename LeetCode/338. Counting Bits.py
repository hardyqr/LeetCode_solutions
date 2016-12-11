# Freddy/Fangyu
# 12/11/2016

def convert_10_to_2(x):
    r=''
    if x==0:
        return str(0)
    else:
        while x!=0:
            r=str(x%2)+r
            x=x//2
        return r


class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        aws=[]
        for i in range(0,num+1):
            b=convert_10_to_2(i)
            aws.append(b.count('1'))
        # print(aws)
        return aws
    # countBits(object,5)
