res = set()
for _ in range(n:=int(input())):
    a, b = map(int, input().split())
    if a >= 0 and b >= 0 and a + b == n - 1:
        res.add((a, b))
print(len(res)) 



