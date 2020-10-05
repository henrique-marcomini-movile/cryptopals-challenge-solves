import unittest

class Testing(unittest.TestCase):
    def test_challenge(self):

        with open('challenges/set1/c8/input.txt', 'r') as f:
            all = f.read()
        
        all_arr = all.split('\n')
        
        arr = [[row[i*16:i*16+16] for i in range(len(row)//16)] for row in all_arr]
        
        best_row = ''
        best_row_rep_count = 0
        
        for row in arr:
            rep = 0
            for val in set(row):
                rep += row.count(val) - 1
            if rep > best_row_rep_count:
                best_row = row
                best_row_rep_count = rep
        
        actual = ''.join(best_row)
        expected = 'd880619740a8a19b7840a8a31c810a3d08649af70dc06f4fd5d2d69c744cd283e2dd052f6b641dbf9d11b0348542bb5708649af70dc06f4fd5d2d69c744cd2839475c9dfdbc1d46597949d9c7e82bf5a08649af70dc06f4fd5d2d69c744cd28397a93eab8d6aecd566489154789a6b0308649af70dc06f4fd5d2d69c744cd283d403180c98c8f6db1f2a3f9c4040deb0ab51b29933f2c123c58386b06fba186a'
        self.assertAlmostEqual(actual, expected)

all = Testing
