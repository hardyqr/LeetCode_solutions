// Freddy @DP
// Feb 7, 2018


class Solution {
public:
    bool hasAlternatingBits(int n) {
        int cur = n;
        int r = cur%2;
        cur = cur / 2;

        while (r != cur %2) {
            r = cur % 2;
            cur = cur / 2;
        }
        if (cur == 0) return true;
        else return false;
    }
};
