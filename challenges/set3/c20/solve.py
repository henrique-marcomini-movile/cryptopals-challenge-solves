import test_suite
from random import randint
from aux.cypher.aes.ctr import CTR
from aux.base64 import decode
from aux.cypher.simple import break_single_byte_xor, xor_bytes
import pprint

key = bytes([randint(0, 255) for _ in range(16)])
ctr = CTR(key)

with open("challenges/set3/c19/input.txt", 'rb') as f:
    all = f.read()
    crypt_texts = [ctr.encrypt(decode(i)) for i in all.split(b"\n")]


class Testing(test_suite.TestCase):

    def test_challenge1(self):
        counter = 0
        nonce_stream = b''
        plaintexts = []
        while ((counter-1) * 16) < len(max(crypt_texts)):
            #Get the blocks
            blocks = []
            for crypt_text in crypt_texts:
                blocks.append(crypt_text[counter*16:(counter+1)*16])
            
            #Break the blocks
            broken_blocks = [b"" for _ in range(16)]
            for block in blocks:
                for i in range(16):
                    if i < len(block):
                        broken_blocks[i] += bytes([block[i]])
            
            for block in broken_blocks:
                nonce_stream += break_single_byte_xor(block)[0][0][:1]
            counter += 1
        for crypt_text in crypt_texts:
            plaintexts.append(xor_bytes(crypt_text, nonce_stream))
        for p in plaintexts:
            print(p)
            pass

all = Testing
