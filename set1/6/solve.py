import sage
import base64
import pprint

with open('6.txt', 'r') as f:
    t = f.read()

t = t.replace('\n', '')

decoded = base64.b64decode(t)

keys = []

for key_size in range(2, 42):
    d = 0
    for i in range((len(decoded)//key_size)-1):
        d += sage.hamming_distance_bytes(
            decoded[i*key_size:(i+1)*key_size], decoded[(i+1)*key_size:(i+2)*key_size])
    d /= (key_size * ((len(decoded)//key_size)-1))
    keys.append((key_size, d))

keys.sort(key=lambda x: x[1])

key_size = keys[0][0]

blocks = [b''.join([bytes([decoded[x*key_size:(x+1)*key_size][i]])
                    for x in range((len(decoded)//key_size)-1)]) for i in range(key_size)]

key = b''

for block in blocks:
    key += sage.guess_xor_key(block)[0][1]
print(key)

dec = sage.xor(decoded, key)
print(dec.decode())
#pprint.pprint(h)
