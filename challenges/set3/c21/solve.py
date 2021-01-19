import test_suite
from aux.rng.mt32 import MT as rand
import pprint

class Testing(test_suite.TestCase):

    def test_challenge1(self):

        mt = rand()
        mt.seed(123)
        
        self.assertEqual(mt.get_number(), 2991312382)
        self.assertEqual(mt.get_number(), 3062119789)
        self.assertEqual(mt.get_number(), 1228959102)
        self.assertEqual(mt.get_number(), 1840268610)
        self.assertEqual(mt.get_number(), 974319580)
        self.assertEqual(mt.get_number(), 2967327842)
        self.assertEqual(mt.get_number(), 2367878886)
        self.assertEqual(mt.get_number(), 3088727057)
        self.assertEqual(mt.get_number(), 3090095699)
        self.assertEqual(mt.get_number(), 2109339754)
        self.assertEqual(mt.get_number(), 1817228411)
        self.assertEqual(mt.get_number(), 3350193721)
        self.assertEqual(mt.get_number(), 4212350166)
        self.assertEqual(mt.get_number(), 1764906721)
        self.assertEqual(mt.get_number(), 2941321312)
        self.assertEqual(mt.get_number(), 2489768049)
        self.assertEqual(mt.get_number(), 2065586814)
        self.assertEqual(mt.get_number(), 601083951)
        self.assertEqual(mt.get_number(), 1684131913)
        self.assertEqual(mt.get_number(), 1722357280)

    def test_challenge2(self):

        mt = rand()
        mt.seed(5489)

        self.assertEqual(mt.get_number(), 3499211612)
        self.assertEqual(mt.get_number(), 581869302)
        self.assertEqual(mt.get_number(), 3890346734)
        self.assertEqual(mt.get_number(), 3586334585)
        self.assertEqual(mt.get_number(), 545404204)
        self.assertEqual(mt.get_number(), 4161255391)
        self.assertEqual(mt.get_number(), 3922919429)
        self.assertEqual(mt.get_number(), 949333985)
        self.assertEqual(mt.get_number(), 2715962298)
        self.assertEqual(mt.get_number(), 1323567403)
        self.assertEqual(mt.get_number(), 418932835)
        self.assertEqual(mt.get_number(), 2350294565)
        self.assertEqual(mt.get_number(), 1196140740)
        self.assertEqual(mt.get_number(), 809094426)
        self.assertEqual(mt.get_number(), 2348838239)
        self.assertEqual(mt.get_number(), 4264392720)
        self.assertEqual(mt.get_number(), 4112460519)
        self.assertEqual(mt.get_number(), 4279768804)
        self.assertEqual(mt.get_number(), 4144164697)
        self.assertEqual(mt.get_number(), 4156218106)

all = Testing
