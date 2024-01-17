import unittest
from scripts.checking_number import is_number  

class TestIsNumber(unittest.TestCase):
    """
    Class to test the is_number function
    """

    def test_is_number_true(self):
        """
        Test for a valid number
        """
        number = 42
        self.assertTrue(is_number(number))

    def test_is_number_true_float(self):
        """
        Test for a valid float
        """
        float_number = 3.14
        self.assertTrue(is_number(float_number))

    def test_is_number_false_str(self):
        """
        Test for a non-number string input
        """
        not_a_number = "Hello"
        self.assertFalse(is_number(not_a_number))

    def test_is_number_false_none(self):
        """
        Test for None input
        """
        none_value = None
        self.assertFalse(is_number(none_value))

    def test_is_number_false_list(self):
        """
        Test for a list input
        """
        a_list = [1, 2, 3]
        self.assertFalse(is_number(a_list))

if __name__ == '__main__':
    unittest.main()
