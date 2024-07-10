a = int(input())
b = int(input())
n = int(input())
m = int(input())

t_min = min(a, b)
t_max = max(a, b)

min_1 = a * (n - 1) + n
max_1 = min_1 + 2 * a

min_2 = b * (m - 1) + m
max_2 = min_2 + 2 * b

up = min(max_1, max_2)
low = max(min_1, min_2)

if low > up:
    print(-1)
else:
    print(low, up)

