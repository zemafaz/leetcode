#include <iostream>
#include <vector>
#include <unordered_map>

int largestOverlap(std::vector<std::vector<int>>& img1, std::vector<std::vector<int>>& img2) {
	std::vector<int> limg1, limg2;
	int n = img1.size();
	std::unordered_map<int, int> count;

	for (int i=0; i < n*n; ++i){
		if (img1[i/n][i%n] == 1) {
			limg1.push_back(i/n * 100 + i % n);
		}
	}
	for (int i=0; i < n*n; ++i){
		if (img2[i/n][i%n] == 1) {
			limg2.push_back(i/n * 100 + i % n);
		}
	}

	for (int i : limg1) {
		for (int j: limg2) {
			count[i-j]++;
		}
	}

	int res = 0;
	for (auto it: count) {
		res = std::max(res, it.second);
	}
	return res;
}

struct args {
	std::vector<std::vector<int>> img1;
	std::vector<std::vector<int>> img2;
	int output;
};

int main() {
	std::vector<args> testArgs {
		{
			std::vector<std::vector<int>>{{1,1,0},{0,1,0},{0,1,0}},
			std::vector<std::vector<int>>{{0,0,0},{0,1,1},{0,0,1}},
			3,
		},
		{
			std::vector<std::vector<int>>{{1}},
			std::vector<std::vector<int>>{{1}},
			1,
		},
		{
			std::vector<std::vector<int>>{{0}},
			std::vector<std::vector<int>>{{0}},
			0,
		},
	};

	bool failed = false;

	for (int i = 0; i < testArgs.size(); i++) {
		args test = testArgs[i];
		int res = largestOverlap(test.img1, test.img2);
		if (res != test.output) {
			std::cout << "Failed test " << i + 1 << ": Expected " << test.output << ", returned " << res << std::endl;
			failed = true;
		}
	}
	if (!failed) {
		std::cout << "Passed all tests!" << std::endl;
	}

	return 0;
}
