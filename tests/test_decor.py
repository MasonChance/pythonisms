import pytest
from decor.decorator import custom_console_logger



def test_cust_console_int():
    num = 5
    actual = custom_console_logger(num)
    expected = ('**********\n(var) is asigned or returns as "5", of type <class \'int\'>\n**********\n')
    assert actual == expected

def test_cust_console_str():
    word = 'this is handy'
    actual = custom_console_logger(word)
    expected = '**********\n(var) is asigned or returns as "this is handy", of type <class \'str\'>\n**********\n'
    assert actual == expected


def test_cust_console_list():
    array = [5, 3, 0, 9]
    actual = custom_console_logger(array)
    expected = '**********\n(var) is asigned or returns as "[5, 3, 0, 9]", of type <class \'list\'>\n**********\n'
    assert actual == expected 


