from aux.cypher.simple import break_single_byte_xor
import test_suite
from aux import hex2bytes, bytes2hex, extend_bytes_to_match
import aux.statistics

class Testing(test_suite.TestCase):

    def test_vector1(self):
        a = b'k'
        b = b'some long byte stuff'
        expected = b'kkkkkkkkkkkkkkkkkkkk'
        actual = extend_bytes_to_match(a, b)
        self.assertEqual(expected, actual)

    def test_vector2(self):
        all_strings = [
            b'v6WWQJH6na0yDLsYhi7D',
            b'QVF0rlXXwtTPe8JuWhRf',
            b'2sd8Mn9llmJXooqEiSIO',
            b'fdxyTm6R9gCKWtMGR5eW',
            b'i9kU2cjjiZjME6LvFZr9',
            b'HzuAd6csv4MLhwdvrxZL',
            b'2o9oN5gNUFn2Q0jnmeJx',
            b'TQLMRS0FrTawka3Hohou',
            b'How? Devise some method for "scoring" a piece of English plaintext. Character frequency is a good metric. Evaluate each output and choose the one with the best score. ',
            b'CeY5mfoTZ3vIbSaV2ryb',
            b'dp5eDKBwlbcTCGBFPyus',
            b'9BmBvLBu1EZI3gcCnDWA',
            b'blufZHGBK93eedGj4gHE',
            b'tyKKHC7kAhS1H3l8jNIR',
            b'A93GU3ltxE3PtOvlWRR9',
            b'pGft36zGT9E48HZfUYeB',
            b'4aNN4eBkrRQHuZGEExGH',
            b'skBsAAycFtl00FiXrBbj',
            b'vrbN08GuXC6POpSWnWdF',
            b'GXmcBg81a5fVg7QuKn3l',
            b'jMv9kgbDAu8jvmf2JN9q'
        ]
        expected = b'How? Devise some method for "scoring" a piece of English plaintext. Character frequency is a good metric. Evaluate each output and choose the one with the best score. '
        actual = aux.statistics.most_close_to_english(all_strings)
        self.assertEqual(expected, actual)

    def test_challenge(self):
        with open('challenges/set1/c3/input.txt', 'r') as f:
            a = hex2bytes(f.read().encode())
       
        top_10 = [x[1] for x in break_single_byte_xor(a)]

        expected = b"Cooking MC's like a pound of bacon"
        self.assertIn(expected, top_10)        

all = Testing



