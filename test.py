import unittest
from xlutil import ExcelUtility

class ExcelUtilityTests(unittest.TestCase):
    """Tests the functionality of the xlutil script."""

    ########################################
    # Tests for init
    ########################################
    def test_init(self):
        x = ExcelUtility()
        self.assertEqual(isinstance(x, ExcelUtility), True)


if __name__ == '__main__':
    unittest.main()