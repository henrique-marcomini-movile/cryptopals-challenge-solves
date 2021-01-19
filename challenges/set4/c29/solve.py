import test_suite
from aux.hash.sha1 import digest, byte_to_bit, bit_to_byte, padd_message
import hashlib


key = b"YELLOW SUBMARINE"
original_text = b"comment1=cooking%20MCs;userdata=foo;comment2=%20like%20a%20pound%20of%20bacon"
original_text_as_bits = byte_to_bit(original_text)
appendix = b";admin=true"
appendix_as_bits = byte_to_bit(appendix)

def oracle(message,hmac):
    return digest(key+message) == hmac

class Testing(test_suite.TestCase):

    def test_challenge1(self):
        original_hmac = digest(key+original_text)
        extended_hmac = b''
        extended_text = b''
        key_bit_len = 0
        #se passar do tamanho da chave é porque deu errado
        #em teoria o tamanho da chave pe um multiplo de 8, mas pra garantir vou fingir
        #que nao é
        for key_bit_len in range(0, 12 * len(key),8):
            message_with_fake_key_as_bits = [1]*key_bit_len + original_text_as_bits
            padded_text = padd_message(message_with_fake_key_as_bits)
            padded_text_with_appendix =  padded_text + appendix_as_bits
            full_final_text_as_bits = padd_message(padded_text_with_appendix)
            full_final_text_as_bytes = bit_to_byte(full_final_text_as_bits)
            extended_hmac = digest(full_final_text_as_bytes[len(padded_text)//8:], original_hmac, False)
            extended_text = bit_to_byte(padded_text_with_appendix)[key_bit_len//8:-1 * (64-len(appendix))]
            if oracle(extended_text, extended_hmac): break

        self.assertEqual(oracle(extended_text, extended_hmac), True)
        
all = Testing