import random
import test_suite
from aux.base64 import decode
from aux.cypher.aes import AES
from aux.cypher.simple import xor_bytes
from aux.padding import check_PKCS7


with open('challenges/set3/c17/17.txt', 'rb') as f:
    t = f.read()

lines = t.split(b'\n')

key = bytes(16)
iv = bytes(16)
text = decode(lines[random.randint(0, len(lines)-1)])
cbc = AES(key, "CBC")
cyphertext = cbc.enc(data=text, iv=iv)


def oracle(cyphertext, iv):
    t = cbc.decrypt(data=cyphertext, iv=iv)
    return check_PKCS7(t)





class Testing(test_suite.TestCase):
    def test_challenge1(self):
        cleartext = b''
        blocks = [cyphertext[i*16: (i+1)*16] for i in range(len(cyphertext)//16)]
        cleartext = b''
        
        for i in range(len(blocks)):
        
            if i == 0:
                round_iv = iv
            else:
                round_iv = blocks[i-1]
        
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
            semi_clear_text = xor_bytes(bytes([padd])*padd, round_iv[-1*padd:])
        
            while padd != 16:
                if padd == 0:
                    padding_mask = b''
                else:
                    padding = bytes([len(semi_clear_text)+1])*len(semi_clear_text)
                    padding_mask = xor_bytes(semi_clear_text, padding)
        
                #now we bruteforce the next byte
                padd+=1
                for j in range(256):
                    attack_iv = round_iv[:-1*padd]+bytes([j])+padding_mask
                    if oracle(blocks[i], attack_iv) == True :
                        semi_clear_text = bytes([j ^ padd]) + semi_clear_text
                        break
        
            cleartext += xor_bytes(semi_clear_text, round_iv)

        cleartext = cleartext[:-1 * cleartext[-1]]
        self.assertEqual(cleartext, text)
all = Testing