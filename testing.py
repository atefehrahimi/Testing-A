import unittest
from validation_digit import number_validation


class TestDigit(unittest.TestCase):
    def test_digit_validation(self):
        sample1 = "123445"                            # a sample1 for check function if return True
        self.assertTrue(number_validation(sample1))

        sample2 = "a string "                        # a sample2 for check function if raise a exception
        self.assertRaises(ValueError, number_validation, sample2)


if __name__ == '__main__':
    unittest.main()
