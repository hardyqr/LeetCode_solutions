// Freddy @BH
// Feb. 9, 2018


class Solution {
public:
    bool isSubsequence(string s, string t) {
        int t_len = t.size();
        int s_len = s.size();
        if(s_len == 0) return true;
        int p = 0;
        char cur = s[p];
        for (int i = 0; i < t_len ; i++) {
            if (cur == t[i]) {
                p++;
                if (p == s_len) return true;
                cur = s[p];
            }
        }
        return false;
    }
};
