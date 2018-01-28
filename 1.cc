// Freddy @BH
// Jan. 28, 2018



/*      
 * Brute Force 
*/

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int a = 0;
        for(auto x:nums){
            int b = 0;
            for(auto y:nums){
                if( x+y==target && a!=b) return vector<int > {a,b};
                b++;
            }
            a++;
        }
    }
};



