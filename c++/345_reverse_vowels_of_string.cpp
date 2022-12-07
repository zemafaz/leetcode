#include <iostream>
#include <vector>
#include <stack>
#include <set>

using namespace std;

string reverseVowels(string s) {
	const set<char> VOWELS {'a', 'e', 'i', 'o', 'u'};
	stack<char> vowels;

	for (char c: s) {
		if (VOWELS.find(c) != VOWELS.end()) {
			vowels.push(c);
		}
	}

	for (int i = 0; i < s.size(); ++i) {
		if(VOWELS.find(s[i]) != VOWELS.end()) {
			s[i] = vowels.top();
			vowels.pop();
		}
	}

	return s;
}

struct args {
	string s;
	string output;
};

int main() {
	vector<args> testArgs {
		{
			"hello",
			"holle",
		},
		{
			"leetcode",
			"leotcede",
		},
	};

	bool failed = false;

	for (int i = 0; i < testArgs.size(); i++) {
		args test = testArgs[i];
		string res = reverseVowels(test.s);
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
