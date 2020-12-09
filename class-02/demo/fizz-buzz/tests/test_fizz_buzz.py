from fizz_buzz import __version__
from fizz_buzz.fizz_buzz import fizz_buzz


def test_version():
    assert __version__ == '0.1.0'


def test_one():
    actual = fizz_buzz(1)
    expected = 1
    assert actual == expected


def test_three():
    actual = fizz_buzz(3)
    expected = 'Fizz'
    assert actual == expected


def test_five():
    actual = fizz_buzz(5)
    expected = 'Buzz'
    assert actual == expected


def test_five_three():
    actual = fizz_buzz(15)
    expected = 'FizzBuzz'
    assert actual == expected


def test_thirty_nine():
    actual = fizz_buzz(39)
    expected = 'Fizz'
    assert actual == expected


def test_floating_point():
    actual = fizz_buzz(28.56)
    expected = 28.56
    assert actual == expected

