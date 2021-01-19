from random import randint
import test_suite
from aux.base64 import decode
from aux.cypher.aes import AES

key = bytes([randint(0,255) for _ in range(16)])
ecb = AES(key=key)


with open('challenges/set2/c12/12.txt', 'rb') as f:
    raw = f.read()

raw = raw.replace(b'\n', b'')
b = decode(raw)


#first compute the last byte

def oracle(text):
    return ecb.enc(data=text+b)

plaintext = b''

class Testing(test_suite.TestCase):
    def test_challenge(self):
        expected = b"Rollin' in my 5.0\nWith my rag-top down so my hair can blow\nThe girlies on standby waving just to say hi\nDid you stop? No, I just drove by\n"
        plaintext = b''
        
        while len(plaintext) != len(b):
            looking = len(plaintext) // 16
            pad = b'A' * (15 - (len(plaintext) % 16))
            a = pad+plaintext
            c = oracle(pad)
            for i in range(0,255):
        
                if c[looking*16:looking*16+16] == oracle(a[-15:]+bytes([i]))[:16]:
                    plaintext += bytes([i])
                    break

        self.assertEqual(expected, plaintext)        
all = Testing