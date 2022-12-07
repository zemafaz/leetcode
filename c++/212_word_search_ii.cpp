#include <iterator>
#include <sstream>
#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

bool findWord(vector<vector<char>>& board, int y, int x, string& word, int iter=0) {
	if (iter == word.size())
		return true;
	if (board[y][x] != word[iter]) {
		return false;
	}

	bool found_it = false;

	if (y > 0)
		found_it = found_it || findWord(board, y-1, x, word, iter + 1);
	if (y < board.size())
		found_it = found_it || findWord(board, y+1, x, word, iter + 1);
	if (x > 0)
		found_it = found_it || findWord(board, y, x-1, word, iter + 1);
	if (x < board[y].size())
		found_it = found_it || findWord(board, y, x+1, word, iter + 1);
	
	return found_it;
}

vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
	vector<string> res = vector<string>();
	for (int i = 0; i < board.size(); ++i) {
		for (int j = 0; j < board[i].size(); ++j) {
			for (int k = 0; k < words.size(); ++k) {
				if (find(res.begin(), res.end(), words[k]) == res.end())
					if (findWord(board, i, j, words[k])) {
						res.push_back(words[k]);
					}
			}
		}
	}
	return res;
}

struct args {
	vector<vector<char>> board;
	vector<string> words;
	vector<string> output;
};

int main() {
	vector<args> testArgs {
		{
			.board=vector<vector<char>>{{'o','a','a','n'},{'e','t','a','e'},{'i','h','k','r'},{'i','f','l','v'}},
			.words=vector<string>{"oath","pea","eat","rain"},
			.output=vector<string>{"eat", "oath"},
		},
		{
			.board=vector<vector<char>>{{"a","b"},{"c","d"}},
			.words=vector<string>{"abcb"},
			.output=vector<string>{},
		},
	};

	bool failed = false;

	for (int i = 0; i < testArgs.size(); i++) {
		args test = testArgs[i];
		vector<string> res = findWords(test.board, test.words);
		if (res != test.output) {
			ostringstream res_stream;
			copy(res.begin(), res.end() - 1, ostream_iterator<string>(res_stream, ","));
			ostringstream output_stream;
			copy(test.output.begin(), test.output.end() - 1, ostream_iterator<string>(output_stream, ","));
			cout << "Failed test " << i + 1 << ": Expected " << output_stream.str() << ", returned " << res_stream.str() << endl;
			failed = true;
		}
	}
	if (!failed) {
		cout << "Passed all tests!" << endl;
	}

	return 0;
}
