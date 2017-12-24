// Freddy @BH, Waterloo
// Dec 24, 2017


string dec2bin(int dec) {
    if(dec == 0) return "";
    else {
        return dec2bin(dec/2) + std::to_string(dec%2);
    }
}

int bin2dec(string bin) {
    int len = bin.size();
    int sum = 0;
    for(int i = 0; i<len; i++){
        if(bin[i] == '1'){
            sum += std::pow(2,len - i - 1);
        }
    }
    return sum;
}

string bitwise_complement(string s) {
    string flipped_s = "";
    int len = s.size();
    for(int i = 0;i<len;i++){
        if(s[i]=='0'){
            flipped_s += "1";
        }else{
            flipped_s += "0";
        }
    }
    return flipped_s;
}

class Solution {
public:
    int findComplement(int num) {
        return bin2dec(bitwise_complement(dec2bin(num)));
    }
};
