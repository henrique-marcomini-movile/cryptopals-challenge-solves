import sage

with open('input.txt', 'rb') as f:
    text = f.read()

print(sage.to_base_64(text))
