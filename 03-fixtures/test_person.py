import unittest
from person import Person


class PersonTest(unittest.TestCase):
    def setUp(self):
        self.p1 = Person('amir', 'big')
        self.p2 = Person('john', 'doe')

    def tearDown(self):
        print('Done ...')

    def test_fullname(self):
        self.assertEqual(self.p1.fullname(), 'amir big')
        self.assertEqual(self.p2.fullname(), 'john doe')

    def test_email(self):
        self.assertEqual(self.p1.email(), 'amirbig@email.com')
        self.assertEqual(self.p2.email(), 'johndoe@email.com')


if __name__ == '__main__':
    unittest.main()

# اجرا در ترمینال برای اجرای تست
# python -m unittest test_person.py
# اجرا در ترمینال برای اجرای تست با جزئیات
# python -m unittest -v test_person.py
