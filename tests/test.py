import unittest

from ImageReader.ImageReader import readFile


class TestSum(unittest.TestCase):
    def test_readFile(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = readFile('mouse.jpg')
        

if __name__ == '__main__':
    unittest.main()  