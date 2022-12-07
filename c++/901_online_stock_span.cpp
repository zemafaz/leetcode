#include <stack>
#include <set>
#include <iostream>
#include <vector>

using namespace std;

class AwfulStockSpanner {

	struct day_price {
		int price;
		int day;
	};
	

	class comparePriceQuotes {
		public:
			bool operator() (const day_price& dp1, const day_price& dp2) const {
				return dp1.price > dp2.price;
			}
	};

	multiset<day_price,
		comparePriceQuotes> price_quotes;

	public:
		int next(int price) {
			int last_over = 0;
			for (day_price dp: this->price_quotes) {
				if (dp.price < price) {
					break;
				}
				if (dp.day > last_over) {
					last_over = dp.day;
				}
			}
			int present_day = price_quotes.size() + 1;
			this->price_quotes.insert({
					.price =  price,
					.day = present_day,
					});
			return present_day - last_over;
		}

};

class StockSpanner {
	stack<pair<int,int>> s;
	public:
		int next(int price) {
			int ans = 1;
			while (!s.empty() && s.top().first <= price) {
				ans += s.top().second;
				s.pop();
			}
			s.push({price, ans});
			return ans;
		}
};

struct args {
	int price;
	int output;
};

int main(int argc, char *argv[]) {
	StockSpanner ss = StockSpanner();
	vector<args> testArgs = {
		{
			100,
			1,
		},
		{
			80,
			1,
		},
		{
			60,
			1,
		},
		{
			70,
			2,
		},
		{
			60,
			1,
		},
		{
			75,
			4,
		},
		{
			85,
			6,
		},
	};
	
	int i = 0;
	for (args test: testArgs) {
		int res = ss.next(test.price);
		if (res != test.output) {
			cout << "Failed test nº" << i << ": Expected " << test.output << ", returned " << res << endl;
		}
		i++;
	}
	cout << "Passed all tests!" << endl;
	return 0;
}

