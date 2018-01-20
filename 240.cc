// Freddy @BH
// Jan. 19

// greedy
class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int m = matrix.size();
        if(m==0)return false;
        int n = matrix[0].size();
        if(n==0)return false;
        for(int i=0; i<m; i++){
            for(int j=n-1;matrix[i][j]>=target && j>=0;j--){
                if(matrix[i][j]==target){
                    return true;
                }
            }
        }
        return false;
    }
};


// Divide and Conquer?
