import test_suite
from aux.hash.sha1 import digest
import hashlib


key = b"YELLOW SUBMARINE"
original_text = b"Take me out tonight\nWhere there's music and there's people\nAnd they're young and alive\nDriving in your car\nI never, never want to go home"
prefixed = key+original_text

class Testing(test_suite.TestCase):

    def test_challenge1(self):
        target = hashlib.sha1(prefixed).hexdigest()
        actual = ''.join([hex(i)[2:].zfill(2) for i in digest(prefixed)])
        self.assertEqual(actual, target)
        
all = Testing