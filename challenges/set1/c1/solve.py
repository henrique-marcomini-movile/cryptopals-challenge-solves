import test_suite
from aux.base64 import encode, decode
from aux import hex2bytes, bytes2hex


class Testing(test_suite.TestCase):

    def test_vector1(self):
        text = b""
        expected = b""
        actual = encode(text)
        self.assertEqual(expected, actual)

    def test_vector2(self):
        text = b"f"
        expected = b"Zg=="
        actual = encode(text)
        self.assertEqual(expected, actual)

    def test_vector3(self):
        text = b"fo"
        expected = b"Zm8="
        actual = encode(text)
        self.assertEqual(expected, actual)

    def test_vector4(self):
        text = b"foo"
        expected = b"Zm9v"
        actual = encode(text)
        self.assertEqual(expected, actual)

    def test_vector5(self):
        text = b"foob"
        expected = b"Zm9vYg=="
        actual = encode(text)
        self.assertEqual(expected, actual)

    def test_vector6(self):
        text = b"fooba"
        expected = b"Zm9vYmE="
        actual = encode(text)
        self.assertEqual(expected, actual)

    def test_vector7(self):
        text = b"foobar"
        expected = b"Zm9vYmFy"
        actual = encode(text)
        self.assertEqual(expected, actual)

    def test_vector8(self):
        expected = b""
        encoded = b""
        actual = decode(encoded)
        self.assertEqual(expected, actual)

    def test_vector9(self):
        expected = b"f"
        encoded = b"Zg=="
        actual = decode(encoded)
        self.assertEqual(expected, actual)

    def test_vector10(self):
        expected = b"fo"
        encoded = b"Zm8="
        actual = decode(encoded)
        self.assertEqual(expected, actual)

    def test_vector11(self):
        expected = b"foo"
        encoded = b"Zm9v"
        actual = decode(encoded)
        self.assertEqual(expected, actual)

    def test_vector12(self):
        expected = b"foob"
        encoded = b"Zm9vYg=="
        actual = decode(encoded)
        self.assertEqual(expected, actual)

    def test_vector13(self):
        expected = b"fooba"
        encoded = b"Zm9vYmE="
        actual = decode(encoded)
        self.assertEqual(expected, actual)

    def test_vector14(self):
        expected = b"foobar"
        encoded = b"Zm9vYmFy"
        actual = decode(encoded)
        self.assertEqual(expected, actual)

    def test_c1(self):
        expected = b"SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
        with open('challenges/set1/c1/input.txt', 'r') as f:
            text = hex2bytes(f.read().encode())
        actual = encode(text)
        self.assertEqual(expected, actual)

    def test_reverse_c1(self):
        expected = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
        encoded = b"SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
        actual = bytes2hex(decode(encoded))
        self.assertEqual(expected, actual)


all = Testing
