import unittest
import sys
from io import StringIO
import os
import unittest.mock
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from quadratic_solver import QuadraticSolver

class TestQuadraticCalc(unittest.TestCase):
    def setUp(self):
        self.output = StringIO()
        self.stdout = self.output
    
    def tearDown(self):
        self.stdout = sys.__stdout__

    def test_two_real_roots(self):
        with unittest.mock.patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            solver = QuadraticSolver(1,3,0)
            solver.calc_quadratic()
            output = mock_stdout.getvalue().strip()   
        self.assertIn("There are 2 roots", output)
                
    def test_one_real_root(self):
        with unittest.mock.patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            solver = QuadraticSolver(1,-2,1)
            solver.calc_quadratic()
            output = mock_stdout.getvalue().strip()
        self.assertIn("There is 1 root", output)
        
    def test_no_real_root(self):
        with unittest.mock.patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            solver = QuadraticSolver(1,0,1)
            solver.calc_quadratic()
            output = mock_stdout.getvalue().strip()
        self.assertIn("There are 0 roots", output)

    def test_cannot_be_zero(self):
        with self.assertRaises(SystemExit):
            QuadraticSolver(0,1,1)

if __name__ == "__main__":
    unittest.main()
        