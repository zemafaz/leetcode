import unittest

class Codec:
	MAP = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
	
	def __init__(self) -> None:
		self.database = []

	def encode(self, long_url: str) -> str:
		self.database.append(long_url)
		i = len(self.database) - 1
		short_url = ""
		
		while i:
			short_url += self.map[i%62]
			i /= len(self.MAP)

		return "http://tinyurl.com/".join(reversed(short_url))

		
	def decode(self, short_url: str) -> str:
		i = 0
		short_url.removeprefix("http://tinyurl.com/")

		for e in short_url:
			i = i * len(self.MAP) + self.MAP.find(e)
		return self.database[i]

class TestSolution(unittest.TestCase):
	codec = Codec()

	def test_1(self):
		long_url = "https://leetcode.com/problems/design-tinyurl"
		short_url = self.codec.encode(long_url)
		self.assertEqual(self.codec.decode(short_url), long_url)

if __name__ == '__main__':
	unittest.main()