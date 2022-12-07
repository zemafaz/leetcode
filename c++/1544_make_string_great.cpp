#include <iostream>
#include <vector>
#include <sstream>
#include <string>

using namespace std;

string makeGood(string s) {
	int end = 0;
	for (int cur = 0; cur < s.size(); ++cur) {
		if (end > 0 && abs(s[cur] - s[end - 1]) == 32)
			end--;
		else {
			s[end] = s[cur];
			end++;
		}
	}
	return s.substr(0, end);
}

struct args {
	string s;
	string output;
};

int main() {
	vector<args> testArgs {
		{
			"leEeetcode",
			"leetcode",
		},
		{
			"abBAcC",
			"",
		},
		{
			"s",
			"s",
		},
	};

	bool failed = false;

	for (int i = 0; i < testArgs.size(); i++) {
		args test = testArgs[i];
		string res = makeGood(test.s);
		if (res != test.output) {
			cout << "Failed test " << i + 1 << ": Expected " << test.output << ", returned " << res << endl;
			failed = true;
		}
	}
	if (!failed) {
		cout << "Passed all tests!" << endl;
	}

	return 0;
}
