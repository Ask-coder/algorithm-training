words = input().split(sep=' ')
data = [input() for _ in range(int(input()))]

my_null = ord('a')


def calc_key(word):
    code = []
    first = ord(word[:1])
    for sym in word:
        res = first - ord(sym)
        code.append(res if res > 0 else res + 26)
    return tuple(code)

def calc_value(word):
    code = []
    first = ord(word[:1])
    for sym in word:
        code.append(first + ord(sym))
    return tuple(code)


mapper = {}
for word in words:    
    mapper[calc_key(word)] = word


for item in data:
    key = calc_key(item)
    #print(key)
    print(mapper[key])







