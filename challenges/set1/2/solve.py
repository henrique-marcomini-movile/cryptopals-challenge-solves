import sage

with open('input.txt', 'rb') as f:
    plaintext = f.read()

with open('key.txt', 'rb') as f:
    key = f.read()


xored = sage.xor(plaintext, key)
print("GOT     : "+sage.bytes_to_hex_string(xored))
print("CORRECT : 746865206b696420646f6e277420706c6179")
