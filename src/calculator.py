class Calculator:
    """Класс калькулятора с бизнес-логикой для модульного тестирования"""

    def add(self, a, b):
        """Сложение двух чисел"""
        return a + b

    def subtract(self, a, b):
        """Вычитание двух чисел"""
        return a - b

    def multiply(self, a, b):
        """Умножение двух чисел"""
        return a * b

    def divide(self, a, b):
        """Деление двух чисел. При делении на ноль выбрасывается исключение"""
        if b == 0:
            raise ZeroDivisionError("Деление на ноль невозможно")
        return a / b

    def is_prime_number(self, n):
        """Проверка, является ли число простым"""
        if not isinstance(n, int) or isinstance(n, bool):
            raise TypeError("Ожидается целое число")
        if n < 2:
            return False
        i = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += 1
        return True
