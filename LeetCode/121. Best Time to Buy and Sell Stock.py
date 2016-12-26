# Freddy/Fangyu@airport
# 12/26/2016



'''Solution 1'''
'''Time Limit Exceeded'''

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l = len(prices)
        count = 0
        m = 0
        while count < l:
            buy = prices[count]
            p = count + 1
            while p < l:
                profit = prices[p] - buy
                if profit > m:
                    m = profit
                p += 1
            count+=1
        print(m)
        return m
t = Solution()
t.maxProfit([7, 1, 5, 3, 6, 4])
t.maxProfit([7, 6, 4, 3, 1])


'''Solution 2'''
