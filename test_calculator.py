import calculator as cal
import pytest

@pytest.mark.parametrize("a,b,c",[(1,2,3), (1.2, 2.1, 3.3), (4,1,6)])
def test_add(a,b,c):
    assert cal.add(a,b) == c

def test_subtract():
    num = 1
    assert cal.subtract(3,2) == num

def test_multiply():
    num = 24
    assert cal.multiply(8,4) == num

def test_divide():
    num = 2.0
    assert cal.divide(8,4) == num