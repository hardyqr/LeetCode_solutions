# April 12, 2018 @DP

class Solution:
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        s = len(pairs)
        dp = [1]*s
        pairs.sort(key = operator.itemgetter(0))
        for i in range(s):
          for j in range(i):
            if(pairs[i][0] > pairs[j][1] and dp[i] < dp[j]+1):
              dp[i] = dp[j]+1
        return max(dp)
