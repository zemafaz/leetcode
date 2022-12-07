#include <unordered_map>
#include <iostream>
#include <vector>

using namespace std;

bool checkSubarraySum(vector<int>& nums, int k) {
	for (int i = 1; i < nums.size(); i++) {
		int sum = nums[i];
		for (int j = i-1; j >= 0; j--) {
			sum += nums[j];
			if (sum % k == 0) {
				return true;
			}
		}
	}
	return false;
}

bool checkSubarraySumMap(vector<int>& nums, int k) {
	if (nums.size() < 2)
		return false;

	unordered_map<int, int> mp;

	mp[0] = -1;

	int runningSum = 0;

	for (int i = 0; i < nums.size(); i++) {
		runningSum += nums[i];
		
		if (k != 0)
			runningSum = runningSum % k;

		if (mp.find(runningSum) != mp.end()) {
			if (i - mp[runningSum] > 1)
				return true;
		} else {
			mp[runningSum] = i;
		}
	}

	return false;
}

struct args {
	vector<int> nums;
	int k;
	bool output;
};

int main() {
	vector<args> testArgs {
		{
			vector<int>{23,2,4,6,7},
			6,
			true,
		},
		{
			vector<int>{23,2,6,4,7},
			6,
			true,
		},
		{
			vector<int>{23,2,6,4,7},
			13,
			false,
		},
	};

	bool failed = false;

	for (int i = 0; i < testArgs.size(); i++) {
		args test = testArgs[i];
		int res = checkSubarraySum(test.nums, test.k);
		if (res != test.output) {
			cout << "Failed test " << i + 1 << ": Expected " << test.output << ", returned " << res << endl;
			failed = true;
		}
	}
	if (!failed) {
		cout << "Passed all tests!" << endl;
	}

	failed = false;

	for (int i = 0; i < testArgs.size(); i++) {
		args test = testArgs[i];
		int res = checkSubarraySumMap(test.nums, test.k);
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
