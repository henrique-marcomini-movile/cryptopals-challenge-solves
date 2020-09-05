import sage
from random import randint

with open('12.txt', 'rb') as f:
    raw = f.read()

raw = raw.replace(b'\n', b'')
b = sage.from_base64(raw)

key = bytes([randint(0,255) for _ in range(16)])

#first compute the last byte

def oracle(text):
    return sage.AES_enc(data=text+b, key=key)

plaintext = b''

while len(plaintext) != len(b):
    looking = len(plaintext) // 16
    pad = b'A' * (15 - (len(plaintext) % 16))
    a = pad+plaintext
    c = oracle(pad)
    #print(c)
    for i in range(0,255):
        #print(c[looking*16:looking*16+16])
        #print(oracle(a[-15:]+bytes([i]))[:16])
        #print("-"*16)
        if c[looking*16:looking*16+16] == oracle(a[-15:]+bytes([i]))[:16]:
            plaintext += bytes([i])
            break
    print(plaintext)
