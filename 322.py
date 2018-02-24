# Freddy @DP
# Feb 23, 2018


''' bottom-up DP '''
class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        n = len(coins)
        D =  [amount+1]*(amount+1)
        D[0] = 0
        for i in range(1,amount+1):
          for j in range(0,n):
            if (i >= coins[j]):
              D[i] = min(D[i],1+D[i-coins[j]])
        if(D[-1] > amount):
          return -1
        else:
          return D[-1]
