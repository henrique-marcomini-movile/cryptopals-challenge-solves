import sage
import time

key = bytes(16)
iv = bytes(16)

def enc_oracle(text):
    prepend = b"comment1=cooking%20MCs;userdata="
    append = b";comment2=%20like%20a%20pound%20of%20bacon"
    sanitized = text.replace(b';',b'').replace(b'=',b'')
    full_input = prepend + sanitized +append
    return sage.AES_enc(data=full_input, key=key, mode="CBC", iv=iv)

def dec_oracle(e):
    return sage.AES_dec(data=e, key=key, mode="CBC", iv=iv)

print("since we want to bitflip a admin=true, we will want to create a block where we can scramble data")
print("comment1=cooking %20MCs;userdata= AAAAAAAAAAAAAAAA AAAAAXadminXtrue ;comment2=%20like%20a%20pound%20of%20bacon")
print("       b1               b2               b3                b4                           ...")

e = enc_oracle(b"AAAAAAAAAAAAAAAAcccccXadminXtrue")

print("we need to put a ; in b4[4]")
for i in range(255):
    e = e[:37]+bytes([i])+e[38:]
    print(sage.AES_dec(data=e, key=key, mode="CBC", iv=iv)[3*16:4*16])
    d = dec_oracle(e)
    time.sleep(0.1)
    if d[53] == ord(';'):
        break


print("\n\nBy now we should have a new argument called admin")
print(dec_oracle(e))

print("\n\nnow we need to change b[15] to have a =")

for i in range(255):
    e = e[:43]+bytes([i])+e[44:]
    print(sage.AES_dec(data=e, key=key, mode="CBC", iv=iv)[3*16:4*16])
    d = dec_oracle(e)
    time.sleep(0.1)
    if d[59] == ord('='):
        break

print("TA DAM")
print(dec_oracle(e))

print('\n',dec_oracle(e).split(b';'))



