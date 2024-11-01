

import unittest
from binary_search import binary_search1


class TestBinarySearch(unittest.TestCase):
    def test_binary_search(self):
        array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        # encontre o valor 4 no array
        find = 4

        # encontre o valor 4 no array
        result = binary_search1(array, find, 0, len(array) - 1)
        # o index que eu espero é
        self.assertEqual(result, 3)


if __name__ == '__main__':
    unittest.main()
