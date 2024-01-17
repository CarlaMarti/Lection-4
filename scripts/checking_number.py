import unittest


def is_number(value):
    """
    Function to check if a value is a number
    """
    try:
        float(value)
        return True
    except (TypeError, ValueError):
        return False


if __name__ == "__main__":
    unittest.main()
