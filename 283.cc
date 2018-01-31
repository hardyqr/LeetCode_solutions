// Freddy @BH
// Jan 30, 2018


class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        while (true) {
            bool flag = true;
            int s = nums.size();
            for (int i=0;i<s-1;i++) {
                if(nums[i]==0 && nums[i+1]!=0) {
                    std::swap(nums[i],nums[i+1]);
                    flag=false;
                }
            }
            if (flag) break;
        }
    }
};

