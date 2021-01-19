import test_suite
from aux.rng.mt32 import MT as rand
from time import time
import pprint

class Testing(test_suite.TestCase):

    def test_challenge1(self):

        seed = int(time())
        mt = rand()
        mt.seed(seed)
        first_number = mt.get_number()

        now = seed + (mt.get_number() % 1000)

        for i in range(now,0,-1):
            mt.seed(i)
            if mt.get_number() == first_number:
                new_seed = i
                break
        
        self.assertEqual(seed, new_seed)
        
        


        
all = Testing
