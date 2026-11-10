import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    # Partner 2
    def test_add(self): # 3 assertions
        assert add(2,3)==5
        assert add(0, 2)==2
        assert add(-1, 7)==6

    def test_subtract(self): # 3 assertions
        assert subtract(5,4)==1
        assert subtract(3, 7) == -4
        assert subtract(2, 0) == 2

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        assert multiply(3,5)==15
        assert multiply(2, 1) == 2
        assert multiply(5, 0) == 0

    def test_divide(self): # 3 assertions
        assert divide(6,3)==2
        assert divide(8, 2) == 4
        assert divide(-12, 3) == -4
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)
    #     fill in code

    def test_logarithm(self): # 3 assertions
        self.assertAlmostEqual(logarithm(2,8),3)
        self.assertAlmostEqual(logarithm(3,9),2)
        self.assertAlmostEqual(logarithm(10,1000),3)

    def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
        with self.assertRaises(ValueError):
            logarithm(5, 0)
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
         with self.assertRaises(ValueError):
              logarithm(0, 5)
    #     fill in code

    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(hypotenuse(3,4),5 )
        self.assertAlmostEqual(hypotenuse(5,12), 13)
        self.assertAlmostEqual(hypotenuse(-3,4), 5)

    def test_sqrt(self): # 3 assertions
        self.assertAlmostEqual(hypotenuse((25)),5)
        self.assertAlmostEqual(hypotenuse((2.25)),1.5)
        self.assertAlmostEqual(hypotenuse((0)), 0)
        with self.assertRaises(ValueError):
            square_root(-4)

# Do not touch this
if __name__ == "__main__":
    unittest.main()