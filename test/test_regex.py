import sys
import re
import unittest

WDIFF_ADDED_RE_I = r'[{][+].*?[+][}]'
WDIFF_REMOVED_RE_I = r'[\[][-].*?[-][]]'

WDIFF_ADDED_RE_M = r'{\+.*?\+}'
WDIFF_REMOVED_RE_M = r'\[-.*?-\]'


class TestRegex(unittest.TestCase):
    def test_wdiff_regex(self):
        line = u"""
        urlwatch [-is-] {+was+} intended to help you watch changes in [-webpages-] {+webpages, files, folders...+} and get notified (via e-mail, in your terminal or through various third party services) of any changes.
        The change notification will include the [-URL-] {+URL/file/folder+} that has changed and a unified diff of what has changed.
        {+There is a lot of reporters+}
        """
        groups1 = re.findall(WDIFF_ADDED_RE_I, line)
        groups2 = re.findall(WDIFF_ADDED_RE_M, line)
        self.assertListEqual(groups1, groups2)
        self.assertEqual(len(groups1), 4)

        groups1 = re.findall(WDIFF_REMOVED_RE_I, line)
        groups2 = re.findall(WDIFF_REMOVED_RE_M, line)
        self.assertListEqual(groups1, groups2)
        self.assertEqual(len(groups1), 3)
