# This is the file that was unit tested, saved as rearrange.py

#!/usr/bin/env python3

import re

def rearrange_name(name):
	result = re.search(r'^([\w .]*), ([\w .]*)$', name)
	if result is None:
		return name
	return '{} {}'.format(result[2], result[1])
  
# This is the unit test script*******************
  
#!/usr/bin/env python3

from rearrange import rearrange_name
import unittest


class TestRearrange(unittest.TestCase):
	def test_basic(self):
		testcase = "Brathwaite, Shimon"
		expected = "Shimon Brathwaite"
		self.assertEqual(rearrange_name(testcase), expected)

	def test_empty(self):
		testcase = ''
		expected = ''
		self.assertEqual(rearrange_name(testcase), expected)

	def test_double_name(self):
		testcase = "Brathwaite, Shimon M."
		expected = "Shimon M. Brathwaite"
		self.assertEqual(rearrange_name(testcase), expected)

	def test_one_name(self):
		testcase = "Shimon"
		expected = "Shimon"
		self.assertEqual(rearrange_name(testcase), expected)

unittest.main()
