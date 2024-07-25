n = int(input())
c = list(map(int, input().split()))
k = int(input())
p = list(map(int, input().split()))

data = {i + 1: c[i] for i in range(n)}

for item in p:
    data[item] -= 1

for key in data:
    print('YES' if data[key] < 0 else 'NO')

