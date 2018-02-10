// Freddy @BH
// Feb. 9, 2018

class Solution {
public:
    int countSubstrings(string s) {
        int res = 0;
        int s_len = s.size();
        for (int i = 0; i < s_len ; i++){
            find(s,i,i,res);
            find(s,i,i+1,res);
        }
        return res;
    }
    void find(string s, int i, int j, int& res) {
        while(i >= 0 && j < s.size() && s[i]==s[j]) {
            i--; j++; res++;
        }
    }
};

