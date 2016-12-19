# Freddy/Fangyu@BNU
# 12/19/2016

def agent(n,tester):
    new=0
    for num in str(n):
        new+=int(num)*int(num)
    print(new)
    if new==1:
        print(True)
        return True
    elif new in tester:
        print(False)
        return False
    else:
        tester.append(new)
        return agent(new,tester)


class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        tester=[]
        return agent(n,tester)
#Solution.isHappy(object,19)
#Solution.isHappy(object,2)
#Solution.isHappy(object,1)
