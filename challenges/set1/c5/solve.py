from aux.cypher.simple import xor_bytes
import unittest
from aux import hex2bytes, bytes2hex, extend_bytes_to_match
import aux.statistics
import pprint

class Testing(unittest.TestCase):

    def test_challenge(self):
        with open('challenges/set1/c5/input.txt', 'r') as f:
            text = f.read()
        for line in text.split('\n'):
            print(line)
            key = extend_bytes_to_match(b'ICE', line.encode())
            enc = xor_bytes(line.encode(), key)
            print(bytes2hex(enc))

all = Testing

        