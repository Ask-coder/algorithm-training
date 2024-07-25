import sys

data = {}
for line in sys.stdin:
    for item in line.split():
        if item not in data:
            data[item] = 0
        data[item] += 1

ans = ''
my_max = 0
for key in data:
    if data[key] > my_max:
        my_max = data[key]
        ans = key
    elif data[key] == my_max:
        ans = min(key, ans)

print(ans)