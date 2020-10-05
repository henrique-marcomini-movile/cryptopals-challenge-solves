import sage
from random import randint

key = bytes([randint(0,255) for _ in range(16)])

print("Getting a good block size\n\n")

#first compute the last byte

def oracle(text):
    cookie = b'email='+text+b'&uid=10&role=user'
    print(cookie, len(cookie))
    return sage.AES_enc(data=cookie, key=key)

def dec(enc):
    return sage.AES_dec(data=enc, key=key)

#first we discover a good email padding size
stop = False
s = len(oracle(b'a' + b'aa@b.com'))

p = 1
while True:
    e = oracle(b'a'*p+b'aa@b.com')
    if len(e) > s:
        break
    p += 1

without_user = oracle(b'a'*(p+len('user'))+b'aa@b.com')[:-16]

print(dec(without_user))

print("\nNow that we have a good block size, lets copy and paste\n\n")

admin = oracle(b'a'*(16-len('email='))+sage.pkcs7(b'admin',16))[16:32]

print(dec(without_user+admin))
