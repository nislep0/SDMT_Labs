from tokenize import String
import unittest
import sys
import os
from io import StringIO
import unittest.mock
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from main import calc_quadratic

class TestQuadraticCalc(unittest.TestCase):
    def setUp(self):
        self.output = StringIO()
        self.stdout = self.output
    
    def tearDown(self):
        self.stdout = sys.__stdout__

    def test_two_real_roots(self):
        with unittest.mock.patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            calc_quadratic(1,3,0)
            output = mock_stdout.getvalue().strip()        
        self.assertIn("There are 2 roots", output)
        
    def test_one_real_root(self):
        with unittest.mock.patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            calc_quadratic(1,-2,1)
            output = mock_stdout.getvalue().strip() 
        self.assertIn("There is 1 root", output)
        
    def test_no_real_root(self):
        with unittest.mock.patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            calc_quadratic(1,0,1)
            output = mock_stdout.getvalue().strip() 
        self.assertIn("There are 0 roots", output)

    def test_cannot_be_zero(self):
        with self.assertRaises(SystemExit):
            calc_quadratic(0,1,1)

if __name__ == "__main__":
    unittest.main()
        