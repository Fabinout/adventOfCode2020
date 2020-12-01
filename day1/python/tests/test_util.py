from unittest import TestCase

from util import readFile


class Test(TestCase):
    def test_read_file(self):
        a = readFile("test_util.py")

        print(a)
        self.assertTrue(a.startswith("from unittest"))
