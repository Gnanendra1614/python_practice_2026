import pytest

from calculator import add, subtract, multiply, divide


def test_add():
    assert add(10, 20) == 30


def test_subtract():
    assert subtract(20, 10) == 10


def test_multiply():
    assert multiply(5, 4) == 20


def test_divide():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)