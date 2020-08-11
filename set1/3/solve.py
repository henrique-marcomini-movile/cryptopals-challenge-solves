import sage
import pprint

with open('input.txt', 'rb') as f:
    enc = f.read()

key = sage.guess_xor_key(enc)[0]
dec = sage.xor(enc,key)
print(dec.decode())