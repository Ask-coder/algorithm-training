n, m = map(int, input().split())

anya = {int(input()) for _ in range(n)}
borya = {int(input()) for _ in range(m)}

intersect = anya.intersection(borya)
print(len(intersect))
print(*sorted(intersect))

anya_diff = anya.difference(borya)
borya_diff = borya.difference(anya)

print(len(anya_diff))
print(*sorted(anya_diff))
print(len(borya_diff))
print(*sorted(borya_diff))