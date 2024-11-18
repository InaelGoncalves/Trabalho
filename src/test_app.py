import sys
import os
import unittest

from app import soma, subtracao, multiplicacao, divisao

class TestApp(unittest.TestCase):

    def test_soma(self):
        self.assertEqual(soma(2, 3), 5)
        self.assertEqual(soma(-1, 1), 0)
        self.assertEqual(soma(0, 0), 0)

    def test_subtracao(self):
        self.assertEqual(subtracao(5, 3), 2)
        self.assertEqual(subtracao(1, 2), -1)
        self.assertEqual(subtracao(0, 0), 0)

    def test_multiplicacao(self):
        self.assertEqual(multiplicacao(2, 3), 6)
        self.assertEqual(multiplicacao(-1, 5), -5)
        self.assertEqual(multiplicacao(0, 10), 0)

    def test_divisao(self):
        self.assertEqual(divisao(6, 3), 2)
        self.assertEqual(divisao(7, 2), 3.5)
        with self.assertRaises(ValueError):
            divisao(10, 0)

if __name__ == '__main__':
    unittest.main()
