# April 15th, 2018 @M3

class Solution:
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        # cash[i]: maximum profit at i-th day without holding stock
        # hold[i]: maximum profit at i-th day with stock
        # cash[i+1] = max(cash[i],hold[i] + prices[i+1] - fee), ie. do nothing or sell
        # hold[i+1] = max(hold[i],cash[i] - prices[i+1]), ie. do nothing or buy
        s = len(prices)
        if(s == 0): return 0
        cash,hold = [0]*s, [0]*s
        cash[0], hold[0] = 0,-prices[0]
        for i in range(s):
            if(i == 0):continue
            cash[i] = max(cash[i-1],hold[i-1]+prices[i]-fee)
            hold[i] = max(hold[i-1],cash[i-1]-prices[i])
        return cash[-1]

