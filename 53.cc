// Freddy @BH, Waterloo
// Jan. 11, 2018


/* Divide and Conquer  - O(nlogn)  */
/*
#include <vector>
#include <iostream>
#include <cmath>
#include <climits>
using namespace std;


int max3(int x, int y, int z){
    if(x>=std::max(y,z)) {
        return x;
    } else{
        if(y>=z){
            return y;
        } else{
            return z;
        }
    }
}

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int length = nums.size();
        if(length==0) return 0;
		if(length==1) return nums[0];
        vector<int> sub_left(nums.begin(),nums.begin()+floor(length/2));
		vector<int> sub_right(nums.begin()+floor(length/2),nums.end());
        int m1 = maxSubArray(sub_left);
        int m2 = maxSubArray(sub_right);
   	    int len=sub_right.size(), c=0,ml=INT_MIN,mr=INT_MIN;
    	for(int i=0; i<len;i++){
       		c+=sub_right[i];
        	ml=max(c,ml);
    	}
		len=sub_left.size();
		c=0;
    	for(int i=len-1; i>=0;i--){
        	c+=sub_left[i];
        	mr=max(c,mr);
    	}
        int m3 = ml+mr;
        return max3(m1,m2,m3);
    }
};
*/

/* Greedy  - O(n), Feb 1st, 2018, @DP */
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int sum = nums[0];
        int maxsum = nums[0];
        int count = 0;
        for (auto num: nums) {
            if (count != 0) {
                sum = sum<=0 ? num : sum+num;
                maxsum = std::max(maxsum,sum);
            }
            count ++;
        }
        return maxsum;
    }
};
