// Freddy @BH, Waterloo
// Jan. 11, 2018

#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int arrayPairSum(vector<int>& nums) {
        int length = nums.size();
        int res = 0;
        sort(nums.begin(),nums.end());
        for(int i = 0; i < length ; i+=2){
            res+=nums[i];
        }
        return res;
    }
};

