import sage
from random import randint

key = bytes([randint(0, 255) for _ in range(16)])


def random_text(text):
    t1 = bytes([randint(ord('a'), ord('z'))
                      for _ in range(randint(5, 10))])
    t2 = bytes([randint(ord('a'), ord('z'))
                      for _ in range(randint(5, 10))])
    return t1 + text + t2


def blackbox(text):
    full_text = random_text(text)
    if randint(0, 1) == 0:
        print("CBC")
        iv = bytes([randint(0, 255) for _ in range(16)])
        enc = sage.AES_enc(data=full_text, key=key, mode="CBC", iv=iv)
    else:
        enc = sage.AES_enc(data=full_text, key=key, mode="ECB")
        print("ECB")
    return enc





for i in range(100):
    sage.dumb_oracle(blackbox)
    print("---")
