import test_suite
from random import randint
from aux.cypher.aes import AES

key = bytes([randint(0, 255) for _ in range(16)])

cbc = AES(key,"CBC")
ecb = AES(key,"ECB")

def random_text(text):
    t1 = bytes([randint(ord('a'), ord('z'))
                      for _ in range(randint(5, 10))])
    t2 = bytes([randint(ord('a'), ord('z'))
                      for _ in range(randint(5, 10))])
    return t1 + text + t2

def blackbox(text):
    full_text = random_text(text)
    if randint(0, 1) == 0:
        enc_type = "CBC"
        iv = bytes([randint(0, 255) for _ in range(16)])
        enc = cbc.enc(data=full_text, iv=iv)
    else:
        enc = ecb.enc(data=full_text) 
        enc_type = "ECB"
    return enc, enc_type


class Testing(test_suite.TestCase):
    def test_challenge(self):
        score = 0
        text = b'a'*1000
        e, ans = blackbox(text)
        for i in range(1000):
            if len(set([e[i*16:i*16+1] for i in range(len(e)//16)])) < ((len(e)//16) * 0.5):
                if ans == "ECB": score += 1
            else:
                if ans == "CBC": score += 1
        self.assertGreater(score, 900)

all = Testing
