# Freddy @SLC
# Feb 24, 2018
class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        D = [0]*(n+1) # min cost to climb to i is D[i]
        for i in range(2,n+1):
            D[i] = min(D[i-1]+cost[i-1],D[i-2]+cost[i-2])
        return D[-1]
