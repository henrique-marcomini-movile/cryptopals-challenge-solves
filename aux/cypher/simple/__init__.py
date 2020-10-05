from aux.statistics import how_close_to_english
from aux import extend_bytes_to_match
import pprint


def xor_bytes(a, b):
    return bytes([c ^ d for c, d in zip(a, b)])


def break_single_byte_xor(a, top=10):
    key, best, d = b'', b'', 99999999999
    all_keys = [extend_bytes_to_match(bytes([i]), a) for i in range(255)]
    all_decoded = list(
        map(lambda x: (x, xor_bytes(a, x), how_close_to_english(xor_bytes(a, x))), all_keys))
    all_decoded.sort(key=lambda x : x[2])

    return all_decoded[:top]
