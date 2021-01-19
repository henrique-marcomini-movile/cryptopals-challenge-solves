

class MT():

    def __init__(self):
        self.w = 32
        self.n = 624
        self.m = 397
        self.r = 31
        self.a = 0x9908B0DF
        self.u = 11
        self.d = 0xFFFFFFFF
        self.s = 7
        self.b = 0x9D2C5680
        self.t = 15
        self.c = 0xEFC60000
        self.l = 18
        self.f = 1812433253
        self.internal_state = [0 for _ in range(self.n)]
        self.internal_index = self.n+1
        self.lower_mask = (1 << self.r) - 1
        self.upper_mask = (1 << self.r)

    def seed(self, value):
        self.internal_index = self.n
        self.internal_state[0] = value
        for i in range(1, self.n):
            self.internal_state[i] = self.internal_state[i-1]
            self.internal_state[i] ^= self.internal_state[i-1] >> (self.w-2)
            self.internal_state[i] *= self.f
            self.internal_state[i] += i
            self.internal_state[i] &= 0xFFFFFFFF

    def twist(self):
        for i in range(self.n):
            x = self.internal_state[i] & self.upper_mask
            x += self.internal_state[(i+1) % self.n] & self.lower_mask
            x &= 0xFFFFFFFF
            xA = x >> 1

            if x % 2 != 0:
                xA ^= self.a
            self.internal_state[i] = self.internal_state[(i + self.m) % self.n]
            self.internal_state[i] ^= xA
        self.internal_index = 0

    def get_number(self):
        if self.internal_index >= self.n:
            if self.internal_index > self.n:
                self.seed(5489)
            self.twist()
 
        y = self.internal_state[self.internal_index]
        y ^= (y >> self.u) & self.d
        y ^= (y << self.s) & self.b
        y ^= (y << self.t) & self.c
        y ^= (y >> self.l)
        y &= 0xFFFFFFFF
 
        self.internal_index += 1
        return y