import pytest
from src.calculator import Calculator

@pytest.fixture
def calc():
    """Создание нового экземпляра калькулятора для каждого теста"""
    return Calculator()

# 1. Тесты метода add (сложение)
@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),           # положительные числа
    (-1, -4, -5),        # отрицательные числа
    (-7, 7, 0),          # числа с разными знаками
    (0, 0, 0),           # нули
    (0.1, 0.2, 0.3),     # дробные числа
])
def test_add(calc, a, b, expected):
    assert calc.add(a, b) == pytest.approx(expected)

# 2. Тесты метода subtract (вычитание)
@pytest.mark.parametrize("a, b, expected", [
    (10, 4, 6),
    (4, 10, -6),         # результат отрицательный
    (-5, -5, 0),
    (2.5, 0.5, 2.0),
])
def test_subtract(calc, a, b, expected):
    assert calc.subtract(a, b) == pytest.approx(expected)

# 3. Тесты метода multiply (умножение)
@pytest.mark.parametrize("a, b, expected", [
    (3, 4, 12),
    (-3, 4, -12),
    (-3, -4, 12),
    (100, 0, 0),         # умножение на ноль
    (1.5, 2, 3.0),
])
def test_multiply(calc, a, b, expected):
    assert calc.multiply(a, b) == pytest.approx(expected)

# 4. Тесты метода divide (деление)
@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5),
    (7, 2, 3.5),         # результат дробный
    (-9, 3, -3),
    (0, 5, 0),           # ноль делим на число
    (1, 3, 0.3333333),
])
def test_divide(calc, a, b, expected):
    assert calc.divide(a, b) == pytest.approx(expected)

# 5. Негативный тест: деление на ноль должно выбрасывать исключение
@pytest.mark.parametrize("a", [1, -1, 0, 3.14])
def test_divide_by_zero(calc, a):
    with pytest.raises(ZeroDivisionError, match="Деление на ноль невозможно"):
        calc.divide(a, 0)

# 6. Тесты метода is_prime_number (простые числа)
@pytest.mark.parametrize("n, expected", [
    (2, True),           # наименьшее простое
    (3, True),
    (13, True),
    (97, True),
    (7919, True),        # большое простое
    (1, False),          # 1 не является простым
    (0, False),
    (-7, False),         # отрицательные не простые
    (4, False),
    (25, False),         # квадрат простого
    (100, False),
])
def test_is_prime_number(calc, n, expected):
    assert calc.is_prime_number(n) == expected

# 7. Негативный тест: нецелое значение в is_prime_number
@pytest.mark.parametrize("value", [2.5, "7", None])
def test_is_prime_number_wrong_type(calc, value):
    with pytest.raises(TypeError):
        calc.is_prime_number(value)
