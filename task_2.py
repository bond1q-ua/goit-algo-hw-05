import re
from typing import Callable

def generator_numbers(text: str):
    pattern = r"\b\d+\.\d+\b"    # Визначення регулярного виразу для пошуку дійсних чисел у тексті
    for match in re.finditer(pattern, text): # Пошук у тексті входжень дійсних чисел
        yield float(match.group())  # Повернення знайденого числа у вигляді float через генератор

def sum_profit(text: str, func: Callable):  # Виклик функції для отримання ітератора дійсних чисел з тексту
    total = sum(func(text)) #обчислення суми цих чисел
    return total

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
