#include <iostream>
#include <string>
#include <vector>
#include <sstream>

using namespace std;

int maximum69Number (int num) {
	ostringstream to_string;
	to_string << num;
	string num_string = to_string.str();

	for (int i=0; i<num_string.size(); ++i) {
		if (num_string[i] == '6') {
			num_string[i] = '9';
			break;
		}
	}
	return stoi(num_string);
}

struct args {
	int num;
	int output;
};

int main() {
	vector<args> testArgs {
		{
			9669,
			9969,
		},
		{
			9996,
			9999,
		},
		{
			9999,
			9999,
		},
	};

	bool failed = false;

	for (int i = 0; i < testArgs.size(); i++) {
		args test = testArgs[i];
		int res = maximum69Number(test.num);
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
