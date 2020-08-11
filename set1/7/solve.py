import sage
import pprint

with open('7.txt','r') as f:
  encoded = f.read()

decoded = sage.from_base64(encoded.encode())

xored = sage.xor(decoded, b"YELLOW SUBMARINE")

print(xored)
