import sage
import pprint

with open('7.txt', 'r') as f:
    data = f.read()
import base64
data = base64.b64decode(data.replace('\n',''))


key = b'YELLOW SUBMARINE'
d = sage.aes.dec(key, data)
print(d)
