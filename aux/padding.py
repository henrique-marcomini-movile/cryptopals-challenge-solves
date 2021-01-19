def padd_PKCS7(val, size = 16):
    k = size - len(val) % size
    if k == 0 : return val + bytes([size])*size
    return val + bytes([k]) * k

def unpadd_PKCS7(val):
    return val[:-1 * val[-1]]

def check_PKCS7(val):
    last_byte = val[-1]
    return val[-1 * last_byte:] == bytes([last_byte])*last_byte