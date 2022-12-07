#include <iostream>
#include <vector>
#include <string>
#include <bitset>

using namespace std;

int maxLength(vector<string>& arr) {
	vector<bitset<26>> dp = {bitset<26>()};
	int res = 0;
	
	for (auto& s : arr) {
		bitset<26> current;
		for (char c: s)
			current.set(c-'a');
		int n = current.count();
		if (n < s.size()) continue;

		for (int i = dp.size() - 1; i >= 0; --i) {
			bitset<26> c = dp[i];
			if ((c & current).any())
				continue;
			dp.push_back( c | current );
			res = max(res, (int)c.count() + n);
		}
	}
	return res;
}

struct args {
	vector<string> arr;
	int output;
};

int main() {
	vector<args> testArgs {
		args{
			vector<string>{"un", "iq", "ue"},
			4
		},
		args{
			vector<string>{"cha", "r", "act", "ers"},
			6
		},
		args{
			vector<string>{"abcdefghijklmnopqrstuvwxyz"},
			26
		},
	};

	bool failed = false;

	for (args test : testArgs) {
		int res = maxLength(test.arr);
		if (res != test.output) {
			cout << "Failed test: Expected " << test.output << ", returned " << res << endl;
			failed = true;
		}
	}
	if (!failed) {
		cout << "Passed all tests!" << endl;
		return 0;
	}
	return 1;
}
