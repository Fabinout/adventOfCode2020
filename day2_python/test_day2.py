from unittest import TestCase

from day2_python.day2 import parseString
from day2_python.inputs import input_test, input_real_case


class Test(TestCase):
    def test_parse_string(self):
        error_password = parseString("1-3 a: abcde")
        self.assertEqual(error_password.password, "abcde")
        self.assertEqual(error_password.policy.min, 1)
        self.assertEqual(error_password.policy.max, 3)
        self.assertEqual('a', error_password.policy.char)

    def test_isValid(self):
        error_password = parseString("1-3 a: abcde")
        self.assertTrue(error_password.isValid())
        self.assertTrue(parseString("2-9 c: ccccccccc").isValid())

    def test_isinvalid(self):
        error_password = parseString("1-3 b: cdefg")
        self.assertFalse(error_password.isValid())

    def test_count_valid_passwords_for_input_test(self):
        self.assertEqual(2, len(list(filter(lambda pw: parseString(pw).isValid(), input_test))))

    def test_count_valid_passwords_for_input(self):
        self.assertEqual(467, len(list(filter(lambda pw: parseString(pw).isValid(), input_real_case))))
