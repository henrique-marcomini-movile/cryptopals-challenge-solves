import time
import test_suite
from aux.cypher.aes.ctr import CTR

key = bytes(16)
ctr = CTR(key)
def enc_oracle(text):
    prepend = b"comment1=cooking%20MCs;userdata="
    append = b";comment2=%20like%20a%20pound%20of%20bacon"
    sanitized = text.replace(b';',b'').replace(b'=',b'')
    full_input = prepend + sanitized +append
    return ctr.encrypt(data=full_input)

def dec_oracle(e):
    a =  ctr.decrypt(data=e)
    return a



class Testing(test_suite.TestCase):
    def test_challenge1(self):
        e = enc_oracle(b"AAAAAAAAAAAAAAAAcccccXadminXtrue")
        
        for i in range(255):
            e = e[:53]+bytes([i])+e[54:]
            d = dec_oracle(e)
            time.sleep(0.1)
            if d[53] == ord(';'):
                break
        
        for i in range(255):
            e = e[:59]+bytes([i])+e[60:]
            d = dec_oracle(e)
            time.sleep(0.1)
            if d[59] == ord('='):
                break
        
        d = {i.split(b"=")[0]:i.split(b"=")[1] for i in dec_oracle(e).split(b';')}
        self.assertEqual(d[b'admin'], b'true')
        

all = Testing