from unittest import TestCase

from day1 import day_1_2


class Test(TestCase):

    def test_day_1(self):
        input = [1721, 979, 366, 299, 675, 1456]
        var = input[2:
              ]
        print(var)


class Test(TestCase):
    def test_day_1_2(self):
        from resources.day1.inputTests import day1_input_test
        a:int = day_1_2(day1_input_test)
        self.assertEqual(a, 241861950)
