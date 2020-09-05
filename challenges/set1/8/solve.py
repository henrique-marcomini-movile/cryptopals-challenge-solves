import sage
from pprint import pprint

with open('8.txt', 'r') as f:
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

print(best_row_rep_count)
print(set(best_row))
print(best_row)
print(''.join(best_row))