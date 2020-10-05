import sage

with open('10.txt', 'rb') as f:
    raw = f.read()

raw = raw.replace(b'\n', b'')
b = sage.from_base64(raw)

decr = sage.AES_dec(data=b, key=b"YELLOW SUBMARINE", mode="CBC", iv=bytes(16))

print(decr)