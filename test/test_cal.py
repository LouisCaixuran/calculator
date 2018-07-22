import unittest
import sys
#sys.path.append("..")
from calculator.main import *
#import calculator.main

class Test_CalTestCase(unittest.TestCase):
	def test_file_number(self):
		fomula=calculate("5+2/2*5-1")
		self.assertEqual(fomula,9)


if __name__ == '__main__':
	unittest.main()