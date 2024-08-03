n, k = map(int, input().split())
x = list(map(int, input().split()))

x.sort()
ans = []

res = set()
tmp = tuple()

a = []
for i in range(n):
    for j in range(n):
        for k in range(n):
            if i != j and j != k and i != k:
                if max(x[i], x[j]) / min(x[i], x[j]) < k and max(x[j], x[k]) / min(x[j], x[k]) < k: 
                    a.append((x[i], x[j], x[k]))
                    print(x[i], x[j], x[k])

print(len(set(a)))

    


# import itertools
# permutations = list(itertools.permutations(x, r=3))
# print(set(permutations))

# print(len(set(permutations)))

