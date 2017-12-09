from unittest import TestCase

import lib


class TestLib(TestCase):
    def test_email_validation(self):
        sample_1 = "invalid"
        self.assertFalse(lib.email_validation(sample_1))

        sample_2 = "me@morteza"
        self.assertFalse(lib.email_validation(sample_2))

        sample_3 = "me@morteza.123"
        self.assertFalse(lib.email_validation(sample_3))

        sample_4 = "me@morteza12@.com"
        self.assertFalse(lib.email_validation(sample_4))

        sample_5 = "me@motezana.com"
        self.assertTrue(lib.email_validation(sample_5))

    def test_digit_validation(self):
        sample1 = "123445"                            # a sample1 for check function if return True
        self.assertTrue(number_validation(sample1))

        sample2 = "a string "                        # a sample2 for check function if raise a exception
        self.assertRaises(ValueError, number_validation, sample2)


