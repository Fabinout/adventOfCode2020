from unittest import TestCase

from day8_python.day8 import parse_line


class Test(TestCase):
    def test_parse_line(self):
        line = parse_line("nop +0")
        self.assertEqual(line.command, "nop")
        self.assertEqual(line.argument, 0)

    def test_parse_line2(self):
        line = parse_line("acc -9")
        self.assertEqual(line.command, "acc")
        self.assertEqual(line.argument, -9)
