import base64

#This is from https://cryptopals.com/sets/1/challenges/7
key = b'YELLOW SUBMARINE'

with open('7.txt', 'r') as f:
    b64 = f.read()

decoded = base64.b64decode(b64.replace('\n', ''))

blocks = [decoded[i:i+16] for i in range(0, len(decoded), 16)]

print("KEY: {} with keysize {}".format(key, len(key)*8))
print("Broke {} bytes in {} blocks of 128 bits".format(len(decoded), len(blocks)))

# KEY: b'YELLOW SUBMARINE' with keysize 128
# Broke 2880 bytes in 180 blocks of 127 bits