import pytest
from calculator import Calculator

def test_dodawanie():
    calc = Calculator()
    assert calc.add(3, 2) == 5

def test_odejmowanie():
    calc = Calculator()
    assert calc.subtract(5, 3) == 2

def test_mnozenie():
    calc = Calculator()
    assert calc.multiply(4, 2) == 8

def test_dzielenie():
    calc = Calculator()
    assert calc.divide(10, 2) == 5

def test_dzielenie_przez_zero():
    calc = Calculator()
    with pytest.raises(ZeroDivisionError):
        calc.divide(5, 0)