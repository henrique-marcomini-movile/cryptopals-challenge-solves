from aux.cypher.simple import break_single_byte_xor
import test_suite
from aux import hex2bytes, bytes2hex, extend_bytes_to_match
import aux.statistics
import pprint

class Testing(test_suite.TestCase):

    def test_challenge(self):
        with open('challenges/set1/c4/input.txt', 'r') as f:
            all = f.read()

        all_arr = all.split('\n')

        arr_as_bytes = [hex2bytes(v) for v in all_arr]

        dec = [break_single_byte_xor(enc)[0] for enc in arr_as_bytes]
        dec.sort(key = lambda x : x[2])

all = Testing
