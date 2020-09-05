import sage

with open('input.txt', 'r') as f:
    text = f.read()

lines = text.split('\n')

for line in lines:
    enc = sage.xor(line.encode(), b'ICE')
    print(sage.bytes_to_hex_string(enc))