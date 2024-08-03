n = int(input())
a = list(map(int, input().split()))
m = int(input())
pairs = [tuple(map(int, input().split())) for _ in range(m)]

a.sort()
pairs.sort(key=lambda x: x[1])

now = 0
res = 0
for i in range(n):
    while pairs[now][0] < a[i]:
        now += 1    
    res += pairs[now][1]

print(res)

