n = int(input())
my_max = None
data = []
for item in input().split():
    my_max = int(item) if my_max is None else max(my_max, int(item))
    data.append(int(item))
a, b, k = map(int, input().split())

offset_a = (a - 1) // k
offset_b = (b - 1) // k

flag = False
if offset_a  != 0 and offset_b % offset_a == 0 and offset_b // n > offset_a //n:
    flag = True
elif offset_b // n - offset_a // n > 1:
    flag = True
elif offset_b  - offset_a >= n:
    flag = True

offset_a %= n
offset_b %= n

list_1 = set()
if flag == 1:
    list_1 = set(data)
elif offset_b > offset_a:
    list_1 = set(data[offset_a:offset_b + 1])
elif offset_b < offset_a:
    list_1 = set(data[0:offset_b + 1])
    list_1 = list_1.union(data[offset_a:])
else:
    list_1.add(data[offset_b])

list_2 = set()
if n + 1 - offset_b < n + 1 - offset_a:
    list_2 = set(data[n - offset_b:n - offset_a + 1])
elif n + 1 - offset_b > n + 1 - offset_a:
    list_2 = set(data[0:n - offset_a])
    list_2 = list_2.union(data[n - offset_b:])
else:
    list_2.add(data[(n - offset_b) % n])

print(max(list_1.union(list_2)))



# n = 5
# scores = [1, 2, 3, 4, 5]
# a, b, k = 3, 5, 2

# n = 5
# scores = [1, 2, 3, 4, 5]
# a, b, k = 15, 15, 2

# n = 5
# scores = [5, 4, 3, 2, 1]
# a, b, k = 2, 5, 2

# n = 5
# scores = [5, 4, 3, 2, 1]
# a, b, k = 2, 2, 2
#  5

# n = 9
# scores = [707, 805, 279, 713, 584, 352, 923, 1000, 237]
# a, b, k = 29, 38, 1
# 1000

# n = 5
# scores = [692, 407, 437, 964, 10]
# a, b, k = 49, 79, 384
# 692

# n = 8
# scores = [952, 159, 945, 463, 133, 101, 767, 314]
# a, b, k = 47, 448, 28
# 952

# n = 9
# scores = [925, 160, 322, 433, 698, 458, 923, 877, 741]
# a, b, k = 46, 92, 12
# 923?

# Vmax = max(a, b)
# Vmin = min(a, b)






