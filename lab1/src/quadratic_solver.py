import sys
import math
import os

class QuadraticSolver:

    def __init__(self, a: float, b: float, c: float):
        if a == 0:
            print("Error. a cannot be 0", file=sys.stdout)
            sys.exit(1)
        self.a = a
        self.b = b
        self.c = c

    def calc_quadratic(self):
        print(f"Equation is: {self.a}x^2 + {self.b}x + {self.c} = 0")

        disc = self.b ** 2 - 4 * self.a * self.c
        if disc > 0: 
            x1 = (-self.b - math.sqrt(disc)) / (2 * self.a)
            x2 = (-self.b + math.sqrt(disc)) / (2 * self.a)
            print("There are 2 roots")
            print(f"x1 = {x1}")
            print(f"x2 = {x2}")
        elif disc == 0: 
            x = -self.b / (2 * self.a)
            print("There is 1 root")
            print(f"x = {x}")
        else: 
            print("There are 0 roots")

    @staticmethod
    def get_float_input(prompt):
        while True:
            try:
                value = input(prompt).strip()
                return float(value)
            except ValueError:
                print(f"Error. Expected a valid real number, got {value} instead.")            

    @classmethod
    def interactive_mod(cls):
        a = cls.get_float_input("a = ")
        while a == 0:
            print("Error. a cannot be 0")
            a = cls.get_float_input("a = ")
        b = cls.get_float_input("b = ")
        c = cls.get_float_input("c = ")
        return cls(a,b,c)

    @classmethod
    def file_mod(cls, filename: str):
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
                return cls(a,b,c)
        except ValueError:
            print("invalid file format", file=sys.stdout)
            sys.exit(1)
    
if __name__ == "__main__":
    if len(sys.argv) == 1:
        try:
            solver = QuadraticSolver.interactive_mod()
            solver.calc_quadratic()
        except OSError:
            print("Error. Input is not supported in this case.")
    elif len(sys.argv) == 2:
        solver = QuadraticSolver.file_mod(sys.argv[1])
        solver.calc_quadratic()
    else:
        print("Usage: python main.py [filename]")
        sys.exit(1)