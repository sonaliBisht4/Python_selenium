import pytest

def add_numbers(a, b):
    return a + b
@pytest.mark.xfail()
@pytest.mark.parametrize("a,b,expected", [
    (1,2,3),
    (4,5,9),
    (1,5,6),
    (3,7,10),
    (3,8,10),
])

def test_add_numbers(a, b, expected):
    assert add_numbers(a, b) == expected