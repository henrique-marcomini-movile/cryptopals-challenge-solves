import test_suite
from aux.cypher.aes.ctr import CTR
from aux.cypher.aes import AES
from aux.cypher.simple import xor_bytes
from aux.base64 import decode

with open("challenges/set4/c25/input.txt", 'r') as f:
    lines =  f.read()

key = b"YELLOW SUBMARINE"
ctr = CTR(key)
ecb = AES(key)
original_text = ecb.decrypt(decode(lines.replace('\n','').encode()))

def seek_and_replace(offset, text, cypher_text):
    plaintext = ctr.decrypt(cypher_text)
    new_text =  plaintext[:offset]
    new_text += text
    new_text += plaintext[offset+len(text):]
    return ctr.encrypt(new_text)

class Testing(test_suite.TestCase):

    def test_challenge1(self):
        cypher_text = ctr.encrypt(original_text)
        dummy = bytes(len(cypher_text))
        known_stream = seek_and_replace(0, dummy, cypher_text)
        plaintext = xor_bytes(cypher_text, known_stream)

        self.assertEqual(plaintext, original_text)
        
all = Testing