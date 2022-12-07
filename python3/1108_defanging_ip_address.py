import unittest

class Solution:
    def defang_IP_addr_cheating(self, address: str) -> str:
        return address.replace(".", "[.]")
    
    def defang_IP_addr(self, address: str) -> str:
        new_address = ""
        for c in address:
            if c == ".":
                new_address += "[.]"
            else:
                new_address += c
        return new_address

class TestSolution(unittest.TestCase):

    def test_1(self):
        address = "1.1.1.1"
        output = "1[.]1[.]1[.]1"
        self.assertEqual(Solution().defang_IP_addr(address), output)

    def test_2(self):
        address = "255.100.50.0"
        output = "255[.]100[.]50[.]0"
        self.assertEqual(Solution().defang_IP_addr(address), output)

if __name__ == "__main__":
    unittest.main()
