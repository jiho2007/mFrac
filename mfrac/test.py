#test.py
#Script By jiho2007

"""
NOTE: ONLY FOR TESTING PACKAGE FOR DEVELOPERS.
DONT IMPORT IT.
"""

import unittest

from frac import frac

class Test(unittest.TestCase):
    def setUp(self):
        self.half = frac(1, 2)
        self.div3 = frac(1, 3)
        self.fds  = frac(4, 8)
        self.opf  = frac(1.5, 3)
        
        self.x = frac(3,2)
    
    def test_reduc(self):
        self.assertEqual(self.fds.reduc(), self.half)

    def test_common(self):
        self.assertEqual(self.half.common(self.div3).n, 3)

    def test_tofloat(self):
        self.assertEqual(float(self.half), 0.5)

    def test_add(self):
        self.assertEqual(self.half + self.div3, frac(5, 6))

    def test_sub(self):
        self.assertEqual(1 - self.div3, frac(2, 3))
	
    def test_sub2(self):
        self.assertEqual(frac(11,2) - 5, frac(1,2))

    def test_mul(self):
        self.assertEqual(self.half * self.div3, frac(1, 6))

    def test_div(self):
        self.assertEqual(1 / self.div3, frac(3, 1))

    def test_eq(self):
        self.assertEqual(self.half == self.fds, True)

    def test_ne(self):
        self.assertEqual(self.half != self.fds, False)

    def test_lt(self):
        self.assertEqual(self.half < self.div3, False)

    def test_le(self):
        self.assertEqual(self.half <= self.fds, True)

    def test_gt(self):
        self.assertEqual(self.half > self.div3, True)

    def test_ge(self):
        self.assertEqual(self.half >= self.div3, True)

    def test_mod(self):
        self.assertEqual(self.x%(4,3), frac(4,3))
	
    def test_reversed(self):
        self.assertEqual(reversed(self.half), frac(2, 1))

    def test_reversed_float(self):
        self.assertEqual(float(reversed(self.half)), 2)

    def test_error_init(self):
        try:
            b = False
            x = frac('hello', 'world')
        except:
            b = True
        self.assertEqual(b, True)

    def test_bug_add(self):
        self.assertEqual(self.half + frac(1, 2), frac(1, 1))

if __name__ == '__main__':
    unittest.main()
