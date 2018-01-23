// Freddy @BH
// Jan. 22, 2018

class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int size = nums.size();
        int maxcount=0;
        int count=0;
        for(int i=0;i<size;i++){
            if(nums[i]==1){
                count++;
            } else{
                count=0;
            }
            maxcount=std::max(count,maxcount);
        }
        return maxcount;
    }
};
