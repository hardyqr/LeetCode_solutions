// Freddy @BH, Waterloo
// Dec 24, 2017

#include <iostream>
#include <cstring>

string convert(int dec) {
    if (dec == 0) {
        return "";
    } else {
        return convert(dec / 2) + std::to_string(dec % 2);
    }
}

int counter(string a, string b, int len){
    int aws = 0;
    for(int i = 0; i<len ; i++){
        if(a[i]!=b[i]) aws++;
    }
    return aws;
}

class Solution {
public:
    int hammingDistance(int x, int y) {
        string xx = convert(x);
        string yy = convert(y);
        int x_len = xx.size();
        int y_len = yy.size();
        if(x_len == y_len) {
            // everything is fine.
        } else if(x_len > y_len){
            yy = string(abs(x_len-y_len), '0').append(yy);
        } else{
            // y_len > x_len
            xx = string(abs(x_len-y_len), '0').append(xx);
        }
        return counter(xx,yy,max(x_len,y_len));
    }
};

