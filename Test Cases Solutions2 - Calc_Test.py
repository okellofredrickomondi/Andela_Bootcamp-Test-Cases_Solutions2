Python 2.7.12 (v2.7.12:d33e0cf91556, Jun 27 2016, 15:19:22) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> """ Running calc unittest"""

import unittest

'''
We import the module to allow us standard unittesting python libraries
'''

from calc import add_numbers

'''
We call the function, Import_add numbers , which will raise the erros below
'''

class TestAddNumbers(unittest.TestCase):
	@unittest.skip("WIP")

	def test_input_is_number(self):
		self.assertRaises(TypeError, str)
			

	def test_works_correctly(self):
		self.assertEquals(add_numbers(3),6)

if __name__ == '__main__':
    unittest.main()
