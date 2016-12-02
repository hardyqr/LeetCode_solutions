# Fangyu
# 12/3/2016

def judge(x):
    if x%3==0 and x%5!=0:
        return 'Fizz'
    if x%3!=0 and x%5==0:
        return 'Buzz'
    if x%3==0 and x%5==0:
        return 'FizzBuzz'
    else:return str(x)

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        aws=[]
        for i in range(1,n+1):
            aws.append(judge(i))
        # print(aws)
        return aws
