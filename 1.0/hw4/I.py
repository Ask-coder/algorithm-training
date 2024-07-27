n = int(input())

dictionary = {}
for _ in range(n):
    key = input()
    if key.lower() not in dictionary:
        dictionary[key.lower()] = []
    dictionary[key.lower()].append(key)

err = 0
for item in input().split():
    cnt_upper = 0
    for char in item:
        if char.isupper():
            cnt_upper += 1

    if item.lower() in dictionary:
        if item not in dictionary[item.lower()]:
            err += 1
    else:
        if cnt_upper != 1:
            err += 1

print(err)
