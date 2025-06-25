from calculator import Calculator

def test_zlozone_dzialanie():
    calc = Calculator()

    wynik = calc.add(2, 3)
    wynik = calc.multiply(wynik, 4)
    wynik = calc.subtract(wynik, 10)
    wynik = calc.divide(wynik, 2)

    assert wynik == 5