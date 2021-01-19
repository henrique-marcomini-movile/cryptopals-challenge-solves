import test_suite
from aux.padding import check_PKCS7

class Testing(test_suite.TestCase):
    def test_challenge1(self):
        self.assertEqual(check_PKCS7(b"ICE ICE BABY\x04\x04\x04\x04"), True)

    def test_challenge2(self):
        self.assertEqual(check_PKCS7(b"ICE ICE BABY\x05\x05\x05\x05"), False)

    def test_challenge3(self):
        self.assertEqual(check_PKCS7(b"ICE ICE BABY\x01\x02\x03\x04"), False)

all = Testing