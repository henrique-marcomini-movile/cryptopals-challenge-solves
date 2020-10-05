def hex2bytes(a):
    to_int = [int(a[i:i+2], 16)
              for i in range(0, len(a), 2)]
    return bytes(to_int)


def bytes2hex(a):
    return ''.join([format(b, '02x') for b in a])

def extend_bytes_to_match(a, b):
    a = a * ((len(b)//len(a))+1)
    return a[:len(b)]

def hamming_distance_bytes(a, b):
    acc = 0
    for i in range(len(a)):
        acc += hamming_distance_byte(bytes([a[i]]), bytes([b[i]]))
    return acc

#Here we can work with octets
def hamming_distance_byte(a, b):
    acc = 0
    for i in range(8):
        acc += ((a[0] >> i) & 1) ^ ((b[0] >> i) & 1)
    return acc