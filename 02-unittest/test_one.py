import unittest
import one


class OneTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(one.add(4, 5), 9)
        self.assertEqual(one.add(-1, 4), 3)

    def test_subtract(self):
        self.assertEqual(one.subtract(5, 0), 5)

    def test_multiply(self):
        self.assertEqual(one.multiply(4, 5), 20)
        self.assertEqual(one.multiply(7, 0), 0)

    def test_division(self):
        self.assertEqual(one.division(30, 5), 6)
        # تست روی exception error ها
        self.assertRaises(ZeroDivisionError, one.division, 4, 0)


if __name__ == "__main__":
    unittest.main()

# اجرا در ترمینال برای اجرای تست
# python -m unittest test_one.py
# اجرا در ترمینال برای اجرای تست با جزئیات
# python -m unittest -v test_one.py
