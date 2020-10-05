import sage
from random import randint

with open('12.txt', 'rb') as f:
    raw = f.read()

raw = raw.replace(b'\n', b'')
b = sage.from_base64(raw)

key = bytes([randint(0,255) for _ in range(16)])

noise = bytes([60 for _ in range(10)])#range(randint(0,100))])


def oracle(text):
    print(noise+text+b)
    return sage.AES_enc(data=noise+text+b, key=key)

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
    print(plaintext)
