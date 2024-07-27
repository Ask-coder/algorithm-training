import sys

res = {}
for line in sys.stdin:
    surname, product, count =  line.split()
    if surname not in res:
        res[surname] = {}
    
    if product not in res[surname]:
        res[surname][product] = 0

    res[surname][product] += int(count)

for surname in sorted(res):
    print(f'{surname}:')
    for product in sorted(res[surname]):
        print(f'{product} {res[surname][product]}')

