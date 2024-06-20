import pytest
import time
from person import Person


class TestPerson:
    @pytest.fixture
    def setup(self):
        # setUp
        self.p1 = Person('amir', 'big')
        self.p2 = Person('john', 'doe')
        # tearDown
        yield 'setup'
        time.sleep(2)

    def test_fullname(self, setup):
        assert self.p1.fullname() == 'amir big'
        assert self.p2.fullname() == 'john doe'

    def test_email(self, setup):
        assert self.p1.email() == 'amirbig@email.com'
        assert self.p2.email() == 'johndoe@email.com'


# اجرا در ترمینال برای اجرای تست
# pytest test_person.py
# اجرا در ترمینال برای اجرای تست با جزئیات
# pytest -v test_person.py
