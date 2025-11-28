def test_add():
    result = 2+3
    print(f"result is :{result}")
    assert result == 5

def test_sub():
    result = 12-2
    print(f"result is :{result}")
    assert result == 10

def test_fail():
    result = 12*10
    print(f"result is :{result}")
    assert result == 10