import pytest

def divide_numbers(a, b):
    return a/ b


@pytest.mark.xfail(reason = "dividing by zero is not handled", strict = True)
def test_divide_by_zero(a, b, expected):
    assert divide_numbers(1, 0) == 0

@pytest.mark.xfail(condition = True, reason = "known bug")
def test_sub_bug():
    result = 5-3
    assert result == 1