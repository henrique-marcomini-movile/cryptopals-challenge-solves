from . import AES
from ..simple import xor_bytes
import struct


class CTR:
    def __init__(self, key=b''):
        self.key = key
        self.aes = AES(key)

    def encrypt(self, data, nonce=0, unsigined=True, litte_endian=True, fixed_nonce=False):
        nonce_as_bytes = nonce.to_bytes(
                8, byteorder="little" if litte_endian else "big", signed=not unsigined)
        counter = 0
        cyphertext = b''
        rolling_data = data
        while True:
            if len(rolling_data) == 0:
                break
            # struct.pack(pack_fmt, nonce)
            counter_as_bytes = counter.to_bytes(
                8, byteorder="little" if litte_endian else "big", signed=not unsigined)
            encrypted_nonce = self.aes.enc(nonce_as_bytes+counter_as_bytes)
            cyphertext += xor_bytes(rolling_data[:16], encrypted_nonce)
            rolling_data = rolling_data[16:]
            counter += 1
        return cyphertext

    def decrypt(self, data, nonce=0, unsigined=True, litte_endian=True, fixed_nonce=False):
        return self.encrypt(data, nonce, unsigined, litte_endian, fixed_nonce)
