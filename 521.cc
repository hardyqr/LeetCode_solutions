// f @DP
// Jan 31, 2018
class Solution {
public:
    int findLUSlength(string a, string b) {
        if (a == b) return -1;
        int a_len = a.length();
        int b_len = b.length();
        if (a_len == b_len) return a_len;
        return std::max(a_len,b_len);
    }
};
