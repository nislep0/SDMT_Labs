import sys
import math

def calc_quadratic(a: float, b: float, c: float):
    if a == 0:
        print("Error. a cannot be 0", file=sys.stdout)
        sys.exit(1)

    print(f"Equation is: {a}x^2 + {b}x + {c} = 0")

    disc = b ** 2 - 4 * a * c
    if disc > 0: 
        x1 = (-b - math.sqrt(disc)) / (2 * a)
        x2 = (-b + math.sqrt(disc)) / (2 * a)
        print("There are 2 roots")
        print(f"x1 = {x1}")
        print(f"x2 = {x2}")
    elif disc == 0: 
        x = -b / (2 * a)
        print("There is 1 root")
        print(f"x = {x}")
    else: 
        print("There are 0 roots")

def get_float_input(prompt):
    while True:
        try:
            value = input(prompt).strip()
            return float(value)
        except ValueError:
            print(f"Error. Expected a valid real number, got {value} instead.")            

if __name__ == "__main__":
    print("Usage: python main.py [filename]")