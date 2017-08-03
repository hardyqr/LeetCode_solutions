// Freddy Fangyu Liu @UWaterloo
// June 22, 2017
#include <iostream>
#include <string>

using namespace std;

// cannot handle overflow cases
/*
string s_reverse(const string s){
    string result;
	int len = s.length();
    for(int i = 0; i < len ;i++){
        result[i] = s[len - 1 - i];
    }
    return result;
}


class Solution {
	public:
    int reverse(int x) {
        unsigned int result = 0;
	    int factor = 1;
		if(x < 0) factor = -1;
		string s = to_string(abs(x));
		result = stoi(s_reverse(s));		
		if(result > INT_MAX)	return 0;
		result = result * factor;
		int result_int = result;
		return result_int;
    }
};
*/

class Solution {
	public:
    int reverse(int x) {
        long long result = 0;
	    int factor = 1;
		if(x < 0) {
			factor = -1;
		}
		int t = abs(x);
		for(; t != 0 ;){
			int tmp = t%10;
			result *= 10;
			result += tmp;
			t /= 10;
		}
		result = result * factor;
		if(result > INT_MAX || result < INT_MIN) {
			return 0;
		}
		return result;
    }
};


int main(){
	Solution test;
	cout << test.reverse(-123123) << endl;;
	cout << test.reverse(1534236469) << endl;
	cout << test.reverse(-2147483648) << endl;
}

