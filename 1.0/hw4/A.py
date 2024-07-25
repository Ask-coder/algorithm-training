n = int(input())
data = {}

for _ in range(n):
    value, key = input().split()
    data[key] = value
    data[value] = key

print(data[input()])