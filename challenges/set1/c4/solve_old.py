import sage
from pprint import pprint

with open('4.txt', 'r') as f:
    all = f.read()

all_arr = all.split('\n')

arr_as_bytes = [sage.hex_string_to_bytes(v) for v in all_arr]

keys = [sage.guess_xor_key(enc)[0] for enc in arr_as_bytes]

all_together_now = [(i, keys[i][0], sage.xor(
    arr_as_bytes[i], keys[i][1])) for i in range(len(keys))]

all_together_now.sort(key=lambda x : x[1])
all_together_now.reverse()

print(all_together_now[0])
