// Freddy @BH
// Dec 24, 2017

class Solution {
public:
    bool judgeCircle(string moves) {
        int x_score = 0;
        int y_score = 0;
        int len = moves.size();
        for(int i = 0; i<len ; i++){
            if(moves[i] == 'U') {
                y_score++;
            }else if(moves[i] == 'D') {
                y_score--;
            }else if(moves[i] == 'R') {
                x_score++;
            }else{
                x_score--;
            }
        }
        if(x_score == 0 && y_score == 0) return true;
        else return false;
    }
};
