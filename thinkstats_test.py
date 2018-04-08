"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2010 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

import unittest
import random
import thinkstats

class Test(unittest.TestCase):

    def testMean(self):
        t = [1, 1, 1, 3, 3, 591]
        mu = thinkstats.Mean(t)
        self.assertEqual(mu, 100)

    def testVar(self):
        t = [1, 1, 1, 3, 3, 591]
        mu = thinkstats.Mean(t)
        var1 = thinkstats.Var(t)
        var2 = thinkstats.Var(t, mu)
        
        self.assertAlmostEqual(mu, 100.0)
        self.assertAlmostEqual(var1, 48217.0)
        self.assertAlmostEqual(var2, 48217.0)

    def testBinom(self):
        res = thinkstats.Binom(10, 3)
        self.assertEqual(res, 120)

        res = thinkstats.Binom(100, 4)
        self.assertEqual(res, 3921225)

    def testInterp(self):
        xs = [1, 2, 3]
        ys = [4, 5, 6]
        interp = thinkstats.Interpolator(xs, ys)

        y = interp.Lookup(1)
        self.assertAlmostEqual(y, 4)

        y = interp.Lookup(2)
        self.assertAlmostEqual(y, 5)

        y = interp.Lookup(3)
        self.assertAlmostEqual(y, 6)

        y = interp.Lookup(1.5)
        self.assertAlmostEqual(y, 4.5)

        y = interp.Lookup(2.75)
        self.assertAlmostEqual(y, 5.75)

        x = interp.Reverse(4)
        self.assertAlmostEqual(x, 1)

        x = interp.Reverse(6)
        self.assertAlmostEqual(x, 3)

        x = interp.Reverse(4.5)
        self.assertAlmostEqual(x, 1.5)

        x = interp.Reverse(5.75)
        self.assertAlmostEqual(x, 2.75)

    def testTrim(self):
        t = list(range(100))
        random.shuffle(t)
        trimmed = thinkstats.Trim(t, p=0.05)
        n = len(trimmed)
        self.assertEqual(n, 90)


if __name__ == "__main__":
    unittest.main()
