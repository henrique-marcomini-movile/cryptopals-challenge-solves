english_language_character_frequency = {
    b'E': 2.02,
    b'T': 9.10,
    b'A': 8.12,
    b'O': 7.68,
    b'I': 7.31,
    b'N': 6.95,
    b'S': 6.28,
    b'R': 6.02,
    b'H': 5.92,
    b'D': 4.32,
    b'L': 3.98,
    b'U': 2.88,
    b'C': 2.71,
    b'M': 2.61,
    b'F': 2.30,
    b'Y': 2.11,
    b'W': 2.09,
    b'G': 2.03,
    b'P': 1.82,
    b'B': 1.49,
    b'V': 1.11,
    b'K': 0.69,
    b'X': 0.17,
    b'Q': 0.11,
    b'J': 0.10,
    b'Z': 0.07
}


def to_base_64(input_as_bytes):
    """This function take a byte object and returns a string containng the 
    base64 representation of those bytes"""

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

    padding = len(input_as_bytes) % 3
    input_as_bytes += b'\x00' * padding
    groups = [input_as_bytes[i:i+3] for i in range(0, len(input_as_bytes), 3)]
    b64_list = []
    # This looks like magic, but it is not
    for group in groups:
        b64_list += [
            alphabet[group[0] >> 2],
            alphabet[((group[0] & 3) << 4) | (group[1] >> 4)],
            alphabet[((group[1] & 15) << 2) | (group[2] >> 6)],
            alphabet[group[2] & 63]
        ]

    return ''.join(b64_list) + '=' * padding


def from_base64(b64):
    alphabet = b"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

    padding = b64.count(b'=')
    b64_indexes = [alphabet.find(x) for x in b64]
    groups = [b64_indexes[i:i+4] for i in range(0, len(b64), 4)]
    r = b''
    # This looks like magic, but it is not
    for group in groups[:-1]:
        r += bytes([(group[0] << 2) | ((group[1] & 48) >> 4)])
        r += bytes([((group[1] & 15) << 4) | ((group[2] & 60) >> 2)])
        r += bytes([((group[2] & 3) << 6) | group[3]])

    if padding <= 2:
        #print("("+str(groups[-1][0])+" << 2) | ("+str(groups[-1][1])+" >> 4)")
        r += bytes([(groups[-1][0] << 2) | (groups[-1][1] >> 4)])

    if padding <= 1:
        #print("(("+str(groups[-1][1])+" & 15) << 4) | (("+str(groups[-1][2])+" & 60) >> 2)")
        r += bytes([((groups[-1][1] & 15) << 4) | ((groups[-1][2] & 60) >> 2)])

    if padding == 0:
        r += bytes([((groups[-1][2] & 3) << 6) | groups[-1][3]])

    return r


def xor(plaintext, key):
    long_key = (key * ((len(plaintext)//len(key))+1))[:len(plaintext)]
    return bytes([plaintext[i] ^ long_key[i] for i in range(len(plaintext))])


def bytes_to_hex_string(hex_as_bytes):
    return ''.join([format(b, '02x') for b in hex_as_bytes])


def hex_string_to_bytes(bytes_as_hex):
    to_int = [int(bytes_as_hex[i:i+2], 16)
              for i in range(0, len(bytes_as_hex), 2)]
    return bytes(to_int)


def remove_not_ascii_letter(string):
    r = b''
    for c in string:
        if c >= 65 and c <= 90 or c >= 97 and c <= 122:
            r += bytes([c])
    return r


def how_close_to_english(string_in_bytes):
    stripped = remove_not_ascii_letter(string_in_bytes).upper()
    frequency = get_frequency(stripped)
    for i in range(65, 91):
        if bytes([i]) not in frequency:
            frequency[bytes([i])] = 0
    return vector_powered_distance(english_language_character_frequency, frequency)


def get_frequency(phrase):
    character_count = {}
    max_val = 0
    for c in phrase:
        if c not in character_count:
            character_count[bytes([c])] = 0
        tmp = character_count[bytes([c])] + 1
        if max_val < tmp:
            max_val = tmp
        character_count[bytes([c])] += 1

    characte_frequency = {key: value /
                          max_val for (key, value) in character_count.items()}
    return characte_frequency


def vector_powered_distance(vect1, vect2):

    acc = 0
    for key in vect1:
        acc += pow(vect1[key] + vect2[key], 2)
    return acc


def guess_xor_key(enc, keys=1):
    all_xors = [(xor(enc, bytes([i])), bytes([i])) for i in range(255)]
    score = [(how_close_to_english(s[0]), s[1]) for s in all_xors]
    score.sort(key=lambda x: x[0])
    score.reverse()
    return score[:keys]


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