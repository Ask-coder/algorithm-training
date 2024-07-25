import sys

data = {}
for line in sys.stdin:
    for item in line.split():
        if item not in data:
            data[item] = 0
        print(data[item], end=' ')
        data[item] += 1