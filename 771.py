# Feb 28, 2018 @DP

class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        count = 0
        n = len(S)
        for i in range(0,n):
            if (S[i] in J):
                count+=1
        return count
