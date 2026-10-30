from src.math_operations import add, subtract

def test_add():
    assert add(2,3) == 5
    assert add(10,-3) == 7
    assert add(-2,-3) == -5
    assert add(-123,5) == -118

def test_subtract():
    assert subtract(2,3) == -1
    assert subtract(10,-3) == 13
    assert subtract(-2,-3) == 1
    assert subtract(-123,5) == -128