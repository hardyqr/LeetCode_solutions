// Freddy Fangyu Liu @UWaterloo
// June 23, 2017

bool match_judge(string haystack, string needle, int i){
    if(needle.length() + i <= haystack.length()){
        bool same = true;
        for(int count = 0; count < needle.length() ; count++){
            if(needle[count] != haystack[i + count]){
                same = false;
            }
        }
        return same;
    } else{
        return false;
    }
}


class Solution {
public:
    int strStr(string haystack, string needle) {
        int result = -1;
        if(haystack.length() == 0 && needle.length() == 0){
            result = 0;
        }
        for(int i = 0; i < haystack.length() ; i++){
            if(match_judge(haystack, needle,i)){
                result = i;
                break;
            }
        }
        return result;
    }
};
