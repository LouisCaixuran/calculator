import unittest
import sys
#sys.path.append("..")
from calculator.main import *
#import calculator.main

class Test_CalTestCase(unittest.TestCase):
	def test_file_number1(self):
		fomula=calculate("5+2/2*5-1")
		self.assertEqual(fomula,9)

	def test_file_number2(self):
			fomula=calculate("5+2+0/2*5-1*0")
			self.assertEqual(fomula,7)

	def test_file_number3(self):
			fomula=calculate("5/2-1")
			self.assertEqual(fomula,1)

	def test_file_number4(self):
			fomula=calculate("9*9-9*8")
			self.assertEqual(fomula,9)

	def test_file_number5(self):
			fomula=calculate("1/0-1")
			self.assertEqual(fomula,-1)



if __name__ == '__main__':
	unittest.main()