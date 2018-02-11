// Freddy @DP
// Feb 11, 2018

class Solution {
public:
    int integerBreak(int n) {
        vector<int> dp {0,0,1,2,4,6,9}; 
        for (int i=7 ; i<=n ; i++) {
            dp.emplace_back(dp[i-3]*3);
        }
        return dp[n];
    }
};
