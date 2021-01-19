from random import randint
import test_suite
from aux.base64 import decode
from aux.cypher.aes import AES

with open('challenges/set2/c14/14.txt', 'rb') as f:
    raw = f.read()

raw = raw.replace(b'\n', b'')
b = decode(raw)
key = bytes([randint(0,255) for _ in range(16)])
noise = bytes([60 for _ in range(10)])#range(randint(0,100))])
ecb = AES(key)

def oracle(text):
    return ecb.enc(data=noise+text+b)


class Testing(test_suite.TestCase):
    def test_challenge(self):
        #first we generate a big text to determine what b'a'*16 looks like
        
        e = oracle(b'A'*1000)
        s = [e[i*16:(i+1)*16] for i in range(len(e)//16)]
        
        for elem in s:
            if s.count(elem) > 10:
                a16 = elem
                break
        
        
        pre_pad = b''
        
        while a16 not in oracle(pre_pad+b'A'*16):
            pre_pad += b'A'
        
        noise_index = oracle(pre_pad+b'A'*16).index(a16)
        
        expected = b"Rollin' in my 5.0\nWith my rag-top down so my hair can blow\nThe girlies on standby waving just to say hi\nDid you stop? No, I just drove by\n"
        plaintext = b''
        
        
        while len(plaintext) != len(b):
            looking = len(plaintext) // 16
            pad = b'B' * (15 - (len(plaintext) % 16))
            a = pad+plaintext
            c = oracle(pre_pad + pad)[noise_index:]
            for i in range(0,255):
                if c[looking*16:looking*16+16] == oracle(pre_pad + a[-15:]+bytes([i]))[noise_index:noise_index+16]:
                    plaintext += bytes([i])
                    break
        self.assertEqual(plaintext, expected)


all = Testing