from aux.cypher.aes import AES
from aux.base64 import decode
import pprint
import test_suite


class Testing(test_suite.TestCase):
    def test_challenge(self):

        with open('challenges/set1/c7/input.txt', 'r') as f:
            data = f.read()
        
        with open('challenges/set1/c7/input.txt', 'rb') as f:
            expected = f.read()

        data = decode(data.replace('\n','').encode())
        
        key = b'YELLOW SUBMARINE'
        c = AES(key)
        
        d = c.decrypt(data)
        self.assertEqual(expected, d)

all = Testing
