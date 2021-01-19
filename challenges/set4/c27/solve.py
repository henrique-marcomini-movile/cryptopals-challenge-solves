import test_suite
from aux.cypher.aes import AES
from aux.cypher.simple import xor_bytes
from aux.base64 import decode


key = b"YELLOW SUBMARINE"
cbc = AES(key,mode="CBC")
original_text = b"Take me out tonight\nWhere there's music and there's people\nAnd they're young and alive\nDriving in your car\nI never, never want to go home"

class Testing(test_suite.TestCase):

    def test_challenge1(self):
        cypher_text = cbc.enc(original_text, iv=key)
        bad_cypher_text = cypher_text[:16]+bytes(16)+cypher_text[:16]
        decrypted = cbc.decrypt(bad_cypher_text, iv=key)
        dumped_key = xor_bytes(decrypted[:16], decrypted[32:48])
        self.assertEqual(key,dumped_key)
        
all = Testing