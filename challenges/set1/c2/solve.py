from aux.cypher.simple import xor_bytes
import unittest
from aux import hex2bytes, bytes2hex


class Testing(unittest.TestCase):

    def test_vector1(self):
        a = bytes(10)
        b = bytes([1]) * 10
        expected = b
        actual = xor_bytes(a, b)
        self.assertEqual(expected, actual)

    def test_vector2(self):
        a = bytes([20]) * 20
        b = a
        expected = bytes(20)
        actual = xor_bytes(a, b)
        self.assertEqual(expected, actual)

    def test_challenge1(self):
        with open('challenges/set1/c2/input.txt', 'r') as f:
            a = hex2bytes(f.read().encode())
        with open('challenges/set1/c2/key.txt', 'r') as f:
            b = hex2bytes(f.read().encode())
        with open('challenges/set1/c2/result.txt', 'r') as f:
            expected = hex2bytes(f.read().encode())
        actual = xor_bytes(a, b)
        self.assertEqual(expected, actual)

    def test_challenge2(self):
        with open('challenges/set1/c2/input.txt', 'r') as f:
            a = hex2bytes(f.read().encode())
        with open('challenges/set1/c2/key.txt', 'r') as f:
            b = hex2bytes(f.read().encode())
        with open('challenges/set1/c2/result.txt', 'r') as f:
            expected = hex2bytes(f.read().encode())
        actual = xor_bytes(b, a)
        self.assertEqual(expected, actual)


all = Testing
