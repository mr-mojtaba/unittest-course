def add(x, y):
    """
    >>> add(7 ,6)
    13
    >>> add(4, -1)
    3
    """
    return x + y


def subtract(x, y):
    """
    >>> subtract(5, 4)
    1
    >>> subtract(6, 9)
    -3
    """
    return x - y


def multiply(x, y):
    """
    >>> multiply(5, 6)
    30
    >>> multiply(5, 'b')
    'bbbbb'
    """
    return x * y

# اجرا در ترمینال برای اجرای تست
# python -m doctest one.py
#
# اجرا در ترمینال برای اجرای تست با جزئیات
# python -m doctest -v one.py
