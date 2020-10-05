alphabet = b"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"


def encode(input_as_bytes):

    if input_as_bytes == b'': return b''

    padding = (3 - (len(input_as_bytes) % 3))%3
    input_as_bytes += b'\x00' * padding
    groups = [input_as_bytes[i:i+3] for i in range(0, len(input_as_bytes), 3)]
    b64_list = []

    for group in groups:
        b64_list += [
            alphabet[group[0] >> 2],
            alphabet[((group[0] & 3) << 4) | (group[1] >> 4)],
            alphabet[((group[1] & 15) << 2) | (group[2] >> 6)],
            alphabet[group[2] & 63]
        ]

    if padding == 0: return bytes(b64_list)
    return bytes(b64_list)[:-1*padding] + b'=' * padding


def decode(b64):

    if b64 == b'': return b''

    padding = b64.count(b'=')
    b64_indexes = [alphabet.find(x) for x in b64]
    groups = [b64_indexes[i:i+4] for i in range(0, len(b64), 4)]
    r = b''

    for group in groups[:-1]:
        r += bytes([(group[0] << 2) | ((group[1] & 48) >> 4)])
        r += bytes([((group[1] & 15) << 4) | ((group[2] & 60) >> 2)])
        r += bytes([((group[2] & 3) << 6) | group[3]])

    if padding <= 2:
        r += bytes([(groups[-1][0] << 2) | (groups[-1][1] >> 4)])

    if padding <= 1:
        r += bytes([((groups[-1][1] & 15) << 4) | ((groups[-1][2] & 60) >> 2)])

    if padding == 0:
        r += bytes([((groups[-1][2] & 3) << 6) | groups[-1][3]])

    return r
