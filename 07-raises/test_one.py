# Need to install pytest ( pip install pytest )
import one
import pytest


# Class test
class TestOne:
    def test_add(self):
        assert one.add(3, 4) == 7
        assert one.add(-1, 4) == 3
        assert one.add(0, 8) == 8

    def test_subtract(self):
        assert one.subtract(4, 5) == -1
        assert one.subtract(9, 0) == 9

    def test_multiply(self):
        assert one.multiply(3, 4) != 11

    def test_division(self):
        assert one.division(50, 5) == 10
        with pytest.raises(ZeroDivisionError):
            one.division(3, 0)


# Functional test
# def test_add():
#     assert one.add(3, 4) == 7
#     assert one.add(-1, 4) == 3
#     assert one.add(0, 8) == 8
#
#
# def test_subtract():
#     assert one.subtract(4, 5) == -1
#     assert one.subtract(9, 0) == 9
#
#
# def test_multiply():
#     assert one.multiply(3, 4) != 11
#
#
# def test_division():
#     assert one.division(50, 5) == 10


# اجرا در ترمینال برای اجرای تست
# pytest test_one.py
# اجرا در ترمینال برای اجرای تست با جزئیات
# pytest -v test_one.py
# ذخیره log در فایل log.
# pytest test_one.py --tb=short > result.log
# ذخیره log در فایل XML
# pytest test_one.py --junitxml=result.xml
