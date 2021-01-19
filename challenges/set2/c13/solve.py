from random import randint
from aux.cypher.aes import AES
from aux.padding import padd_PKCS7
import test_suite


key = bytes([randint(0,255) for _ in range(16)])
ecb = AES(key)

print("Getting a good block size\n\n")

#first compute the last byte

def oracle(text):
    cookie = b'email='+text+b'&uid=10&role=user'
    #print(cookie, len(cookie))
    return ecb.enc(data=cookie)

def dec(enc):
    return ecb.decrypt(data=enc)

def form2dict(form):
    return {i.split(b"=")[0]:i.split(b"=")[1] for i in form.split(b"&")}

class Testing(test_suite.TestCase):
    def test_challenge(self):
        #first we discover a good email padding size
        s = len(oracle(b'a' + b'aa@b.com'))
        p = 1
        while True:
            e = oracle(b'a'*p+b'aa@b.com')
            if len(e) > s:
                break
            p += 1
        
        without_user = oracle(b'a'*(p+len('user'))+b'aa@b.com')[:-16]
        admin = oracle((p-len(b'email=')-1)*b'a'+padd_PKCS7(b'admin'))[16:32]
        r = dec(without_user+admin)[:-16+len(b"admin")]
        d = form2dict(r)
        self.assertEqual(b"admin", d[b'role'])

        
        


all = Testing