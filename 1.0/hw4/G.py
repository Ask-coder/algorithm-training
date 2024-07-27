import sys

res = {}
for line in sys.stdin:
    tmp = line.split()
    action = tmp[0]
    if action == "DEPOSIT":
        name, amount = tmp[1], tmp[2]
        if name not in res:
            res[name] = 0
        res[name] += int(amount)
    elif action == "WITHDRAW":
        name, amount = tmp[1], tmp[2]
        if name not in res:
            res[name] = 0
        res[name] -= int(amount)
    elif action == "BALANCE":
        name = tmp[1]
        print(res.get(name, 'ERROR'))
    elif action == "TRANSFER":
        name1, name2, amount = tmp[1], tmp[2], tmp[3]
        if name1 not in res:
            res[name1] = 0
        if name2 not in res:
            res[name2] = 0

        res[name1] -= int(amount)
        res[name2] += int(amount)
    elif action == "INCOME":
        p = int(tmp[1])
        for name in res:
            if res[name] > 0:
                res[name] = int((res[name] * (100 + p)) / 100) 
    

