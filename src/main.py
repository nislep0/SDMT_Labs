import sys
import math
import os

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

def interactive_mod():
    a = get_float_input("a = ")
    while a == 0:
        print("Error. a cannot be 0")
        a = get_float_input("a = ")
    b = get_float_input("b = ")
    c = get_float_input("c = ")
    calc_quadratic(a,b,c)

def file_mod(filename: str):
    if not os.path.exists(filename):
        print(f"file {filename} does not exist", file=sys.stdout)
        sys.exit(1)

    try:
        with open(filename, "r") as file:
            line = file.readline().strip()
            parts = line.split()
            if len(parts) != 3:
                raise ValueError("invalid file format")
            a, b, c = map(float, parts)
            calc_quadratic(a,b,c)
    except ValueError:
        print("invalid file format", file=sys.stdout)
        sys.exit(1)
    
if __name__ == "__main__":
    if len(sys.argv) == 1:
        try:
            interactive_mod()
        except OSError:
            print("Error. Input is not supported in this case.")
    elif len(sys.argv) == 2:
        file_mod(sys.argv[1])
    else:
        print("Usage: python main.py [filename]")
        sys.exit(1)