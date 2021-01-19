import test_suite
from aux.rng import mt32
from aux.cypher import diffie_hellman

rng = mt32.MT()

class Testing(test_suite.TestCase):

    def test_challenge1(self):
        dh = diffie_hellman.dh(37,5)

        exp_a = rng.get_number() % 37
        exp_b = rng.get_number() % 37

        pub_key_A = pow(dh.g,exp_a,dh.p)
        pub_key_B = pow(dh.g,exp_b,dh.p)

        session_1 = pow(pub_key_B, exp_a, dh.p)
        session_2 = pow(pub_key_A, exp_b, dh.p)


        self.assertEqual(session_1, session_2)

    def test_challenge2(self):
        p = int("ffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c245e485b576625e7ec6f44c42e9a637ed6b0bff5cb6f406b7edee386bfb5a899fa5ae9f24117c4b1fe649286651ece45b3dc2007cb8a163bf0598da48361c55d39a69163fa8fd24cf5f83655d23dca3ad961c62f356208552bb9ed529077096966d670c354e4abc9804f1746c08ca237327ffffffffffffffff", 16)
        g = 2
        dh = diffie_hellman.dh(p,g)

        exp_a = rng.get_number() % 37
        exp_b = rng.get_number() % 37

        pub_key_A = pow(dh.g,exp_a,dh.p)
        pub_key_B = pow(dh.g,exp_b,dh.p)

        session_1 = pow(pub_key_B, exp_a, dh.p)
        session_2 = pow(pub_key_A, exp_b, dh.p)


        self.assertEqual(session_1, session_2)
        
all = Testing