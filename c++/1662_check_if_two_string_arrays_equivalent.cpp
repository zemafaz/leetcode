#include <algorithm>
#include <string>
#include <iostream>
#include <vector>

using namespace std;

bool arrayStringsAreEqual(vector<string>& word1, vector<string>& word2) {
	int i = 0, j = 0;
	int m = 0, n = 0;

	while (i < word1.size() and j < word2.size()) {
		if (word1[i][m++] != word2[j][n++])
			return false;

		if (m >= word1[i].size())
			i++, m = 0;

		if (n >= word2[j].size())
			j++, n = 0;
	}

	return i == word1.size() and j == word2.size();
}

struct args {
	vector<string> word1;
	vector<string> word2;
	int output;
};

int main() {
	vector<args> testArgs {
		args{
			vector<string>{"ab", "c"},
			vector<string>{"a", "bc"},
			true	
		},
		args{
			vector<string>{"a", "cb"},
			vector<string>{"ab", "c"},
			false
		},
		args{
			vector<string>{"abc", "d", "defg"},
			vector<string>{"abcddefg"},
			true
		},
	};

	bool failed = false;

	for (int i = 0; i < testArgs.size(); i++) {
		args test = testArgs[i];
		int res = arrayStringsAreEqual(test.word1, test.word2);
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
