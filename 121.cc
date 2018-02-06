// Freddy @DP
// Feb. 6, 2018

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if(prices.size() == 0) return 0;
        int maxprofit = 0;
        int curprofit = 0;
        int minprice = prices[0];
        for(auto p: prices) {
            if (p < minprice) minprice = p;
            curprofit = p - minprice;
            if (curprofit > maxprofit) maxprofit = curprofit;
        }
        return maxprofit;
    }
};
