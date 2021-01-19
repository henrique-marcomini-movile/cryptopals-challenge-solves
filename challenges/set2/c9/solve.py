import test_suite
import aux.padding


class Testing(test_suite.TestCase):
    def test_challenge(self):
        expected = b"YELLOW SUBMARINE\x04\x04\x04\x04"
        actual = aux.padding.padd_PKCS7(b"YELLOW SUBMARINE", 20)
        self.assertEqual(expected, actual)

all = Testing