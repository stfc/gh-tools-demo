import sys
sys.path.append('..')

import foo
import unittest


class TestFoo(unittest.TestCase):
    def test_adder(self):
        for i in range(20):
            self.assertEqual(foo.adder(i, 0.5 * i), (i + 0.5 * i))

if __name__ == '__main__':
    unittest.main()
