import sage
import random

with open('17.txt', 'rb') as f:
    t = f.read()

lines = t.split(b'\n')

key = bytes(16)
iv = bytes(16)
text = sage.from_base64(lines[random.randint(0, len(lines)-1)])
cyphertext = sage.AES_enc(data=text, key=key, iv=iv, mode="CBC")


def oracle(cyphertext, iv):
    t = sage.AES_dec(data=cyphertext, key=key, iv=iv, mode="CBC")
    return sage.verify_pkcs7(t)


cleartext = b''

blocks = [cyphertext[i*16: (i+1)*16] for i in range(len(cyphertext)//16)]

cleartext = b''

print(text)
for i in range(len(blocks)):


    if i == 0:
        round_iv = iv
    else:
        round_iv = blocks[i-1]


    #print(sage.AES_dec(key=key,data=blocks[i],iv=round_iv,mode="CBC"))


    # First we check if ther is any padding
    padd = -1

    if oracle(blocks[i], round_iv) == False:
        padd = 0
    else:
        for j in range(16):
            attack_iv = round_iv[:j]+b'0'+round_iv[j+1:]
            if oracle(blocks[i], attack_iv) == False:
                padd = 16-j
                break


    padding_mask = b''

    semi_clear_text = sage.xor(bytes([padd])*padd, round_iv[-1*padd:])

    while padd != 16:
        if padd == 0:
            padding_mask = b''
        else:
            padding = bytes([len(semi_clear_text)+1])*len(semi_clear_text)
            padding_mask = sage.xor(semi_clear_text, padding)

        #now we bruteforce the next byte
        padd+=1
        for j in range(256):
            attack_iv = round_iv[:-1*padd]+bytes([j])+padding_mask
            if oracle(blocks[i], attack_iv) == True :
                semi_clear_text = bytes([j ^ padd]) + semi_clear_text
                break

    cleartext += sage.xor(semi_clear_text, round_iv)

print(cleartext[:-1*cleartext[-1]])