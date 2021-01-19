import test_suite
from aux.cypher.aes.ctr import CTR
from aux.base64 import decode


class Testing(test_suite.TestCase):

    def test_challenge1(self):
        input_data = b"L77na/nrFsKvynd6HzOoG7GHTLXsTVu9qvY/2syLXzhPweyyMTJULu/6/kXX0KSvoOLSFQ=="
        expected = b"Yo, VIP Let's kick it Ice, Ice, baby Ice, Ice, baby "
        decoded_input = decode(input_data)
        key = b"YELLOW SUBMARINE"
        ctr = CTR(key)
        plaintext = ctr.decrypt(decoded_input)
        self.assertEqual(expected, plaintext)


all = Testing
