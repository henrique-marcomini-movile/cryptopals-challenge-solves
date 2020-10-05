import pprint
from aux import hamming_distance_bytes, extend_bytes_to_match
from aux.base64 import encode, decode
from aux.cypher.simple import break_single_byte_xor, xor_bytes
import unittest


class Testing(unittest.TestCase):

    def test_challenge(self):

        with open('challenges/set1/c6/input.txt', 'r') as f:
            t = f.read()
        with open('challenges/set1/c6/expected.txt', 'r') as f:
            expected = f.read().encode()
        t = t.replace('\n', '')
        
        decoded = decode(t.encode())
        
        keys = []
        
        for key_size in range(2, 42):
            d = 0
            for i in range((len(decoded)//key_size)-1):
                d += hamming_distance_bytes(
                    decoded[i*key_size:(i+1)*key_size], decoded[(i+1)*key_size:(i+2)*key_size])
            d /= (key_size * ((len(decoded)//key_size)-1))
            keys.append((key_size, d))
        
        keys.sort(key=lambda x: x[1])
        
        key_size = keys[0][0]
        
        blocks = [b''.join([bytes([decoded[x*key_size:(x+1)*key_size][i]])
                            for x in range((len(decoded)//key_size)-1)]) for i in range(key_size)]
        
        key = b''
        for block in blocks:
            key += bytes([break_single_byte_xor(block)[0][0][0]])
        
        full_key = extend_bytes_to_match(key, decoded)
        dec = xor_bytes(decoded, full_key)
        with open('challenges/set1/c6/expected.txt', 'wb') as f:
            f.write(dec)
        self.assertEqual(dec, expected)



all = Testing
