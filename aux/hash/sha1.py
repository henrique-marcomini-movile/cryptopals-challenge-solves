# docs
# https://tools.ietf.org/html/rfc3174

from struct import pack


def byte_to_bit(b):
    bytes_as_bits = []
    for i in b:
        bytes_as_bits += [(i >> (7-j)) & 1 == 1 for j in range(8)]
    return bytes_as_bits


def bit_to_byte(b):
    r_b = b[::-1]
    v = 0
    for i in range(len(b)):
        v |= r_b[i] << i
    return v.to_bytes(len(b)//8, 'big')


def bit_to_int(b):
    r_b = b[::-1]
    v = 0
    for i in range(len(b)):
        v |= r_b[i] << i
    return v


def left_bit_shift(x, n):
    return x[n:]+([0]*n)


def right_bit_shift(x, n):
    return ([0]*(32-n))+x[:-1 * (32-n)]


def bit_sum(x, y):
    return byte_to_bit(((bit_to_int(x)+bit_to_int(y)) % (2**32)).to_bytes(len(x)//8, 'big'))


def S(x, n):
    a = left_bit_shift(x, n)
    b = right_bit_shift(x, n)
    return [a[i] or b[i] for i in range(32)]


def padd_message(message, fake_len=-1):
    l = len(message) if fake_len == -1 else fake_len
    l_be = pack(">Q", l)
    l_be_as_bits = byte_to_bit(l_be)
    message.append(True)
    message += [0]*(512-(l+1+len(l_be_as_bits)) % 512)
    message += l_be_as_bits
    return message


def f(t, B, C, D):
    if t <= 19:
        return _f_19(B, C, D)
    elif t <= 39:
        return _f_39(B, C, D)
    elif t <= 59:
        return _f_59(B, C, D)
    else:
        return _f_79(B, C, D)


def _f_19(B, C, D):
    return [(B[i] and C[i]) or ((not B[i]) and D[i]) for i in range(32)]


def _f_39(B, C, D):
    return [B[i] ^ C[i] ^ D[i] for i in range(32)]


def _f_59(B, C, D):
    return [(B[i] and C[i]) or (B[i] and D[i]) or (C[i] and D[i]) for i in range(32)]


def _f_79(B, C, D):
    return _f_39(B, C, D)


def k(t):
    if t <= 19:
        return byte_to_bit(b'\x5a\x82\x79\x99')
    elif t <= 39:
        return byte_to_bit(b'\x6e\xd9\xeb\xa1')
    elif t <= 59:
        return byte_to_bit(b'\x8f\x1b\xbc\xdc')
    else:
        return byte_to_bit(b'\xca\x62\xc1\xd6')


def digest(message, second_buffer=[], do_padd=True):
    message_as_bits = byte_to_bit(message)
    if do_padd:
        padded_message = padd_message(message_as_bits)
    else:
        padded_message = message_as_bits

    if second_buffer == []:
        second_buffer = [
            byte_to_bit(b'\x67\x45\x23\x01'),
            byte_to_bit(b'\xEF\xCD\xAB\x89'),
            byte_to_bit(b'\x98\xBA\xDC\xFE'),
            byte_to_bit(b'\x10\x32\x54\x76'),
            byte_to_bit(b'\xC3\xD2\xE1\xF0')
        ]
    else:
        second_buffer = [
            byte_to_bit(second_buffer[0:4]),
            byte_to_bit(second_buffer[4:8]),
            byte_to_bit(second_buffer[8:12]),
            byte_to_bit(second_buffer[12:16]),
            byte_to_bit(second_buffer[16:20])
       ]
    return digest_part2(padded_message, second_buffer)


def digest_part2(padded_message, second_buffer):
    first_buffer = [[0]*32 for _ in range(5)]

    output_as_bits = []

    M = [padded_message[i:i+512] for i in range(0, len(padded_message), 512)]
    for m in M:
        W = [m[i:i+32] for i in range(0, len(m), 32)]
        W += [[0, 0, 0, 0, 0, 0, 0, 0] for _ in range(64)]
        for t in range(16, 80):
            tmp_1 = W[t-3]
            tmp_2 = W[t-8]
            tmp_3 = W[t-14]
            tmp_4 = W[t-16]
            tmp_5 = [tmp_1[i] ^ tmp_2[i] ^ tmp_3[i] ^ tmp_4[i]
                     for i in range(32)]
            W[t] = S(tmp_5, 1)

        first_buffer = [second_buffer[i] for i in range(5)]

        for t in range(80):
            tmp_1 = S(first_buffer[0], 5)
            tmp_2 = f(t, first_buffer[1], first_buffer[2], first_buffer[3])
            tmp_3 = first_buffer[4]
            tmp_4 = W[t]
            tmp_5 = k(t)
            TEMP = bit_sum(
                bit_sum(bit_sum(bit_sum(tmp_1, tmp_2), tmp_3), tmp_4), tmp_5)

            first_buffer[4] = first_buffer[3]
            first_buffer[3] = first_buffer[2]
            first_buffer[2] = S(first_buffer[1], 30)
            first_buffer[1] = first_buffer[0]
            first_buffer[0] = TEMP

        second_buffer[0] = bit_sum(second_buffer[0], first_buffer[0])
        second_buffer[1] = bit_sum(second_buffer[1], first_buffer[1])
        second_buffer[2] = bit_sum(second_buffer[2], first_buffer[2])
        second_buffer[3] = bit_sum(second_buffer[3], first_buffer[3])
        second_buffer[4] = bit_sum(second_buffer[4], first_buffer[4])

    for H in second_buffer:
        output_as_bits += H

    return bit_to_byte(output_as_bits)

