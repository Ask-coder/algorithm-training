n = int(input())
seq = list(map(int, input().split()))

res = [0] * (n + 1)

for i in range(n):
    res[i + 1] = res[i] +  seq[i]

print(*res[1:])