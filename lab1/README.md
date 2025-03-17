# Quadratic Equation Solver

## Опис лабораторної
У цій лабораторній ми знаходимо корені квадратного рівняння виду:

```
ax^2 + bx + c = 0
```

Дана програма підтримує два режими роботи:
1. Інтерактивний режим – введення коефіцієнтів вручну.
2. Читання коефіцієнтів з файлу.

## Інструкція зі збору та запуску проекту

### Вимоги
- Python 3.x

### Встановлення
```sh
# Клонуйте репозиторій
git clone https://github.com/nislep0/SDMT_Labs.git
cd SDMT_Labs
```

### Використання
#### Інтерактивний режим
```sh
python3 main.py
```
Приклад роботи: 
```sh
a = 1
b = 3
c = 0
Equation is: 1.0x^2 + 3.0x + 0.0 = 0
There are 2 roots
x1 = -3.0
x2 = 0.0
```

#### Зчитування коефіцієнтів з файлу
```sh
python3 main.py values.txt
```
Приклад роботи:
```sh
Equation is: 1.0x^2 + 3.0x + 0.0 = 0
There are 2 roots
x1 = -3.0
x2 = 0.0
```

## Опис формату файлу для неінтерактивного режиму
Файл повинен містити три числа (коефіцієнти `a`, `b`, `c`) через пробіл на одному рядку. Наприклад:
```
1 -3 2
```
Ці значення будуть використані для обчислення коренів рівняння.

### Запуск тестів
```sh
python3 -m unittest tests.unit_test
```

## Вказання на revert-коміт
[Revert "Add message that user should run program in different format"](https://github.com/nislep0/SDMT_Labs/commit/badd1e4982fa25bf2e0a6bcbde4039e61b9d7fdc)

[Revert "Add unit tests for quadratic calculation"](https://github.com/nislep0/SDMT_Labs/commit/44c109f256a27eb37b04f48de7554dc0579a77b1)

