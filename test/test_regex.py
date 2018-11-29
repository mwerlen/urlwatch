import sys
import re
import unittest

WDIFF_ADDED_RE_I = r'[{][+].*?[+][}]'
WDIFF_REMOVED_RE_I = r'[\[][-].*?[-][]]'

WDIFF_ADDED_RE_M = r'[{][+].*?[+][}]'
WDIFF_REMOVED_RE_M = r'[\[][-].*?[-][]]'


class TestRegex(unittest.TestCase):
    def test_wdiff_regex(self):
        line = u"This is a [-bad-] {+good+} test"
        groups1 = re.split(WDIFF_ADDED_RE_I, line)
        groups2 = re.split(WDIFF_ADDED_RE_M, line)
        self.assertListEqual(groups1, groups2)

        groups1 = re.split(WDIFF_REMOVED_RE_I, line)
        groups2 = re.split(WDIFF_REMOVED_RE_M, line)
        self.assertListEqual(groups1, groups2)
