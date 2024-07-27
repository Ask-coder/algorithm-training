n, m = map(int, input().split())
w = input()
s = input()

template = {}
for char in w:
    if char not in template:
        template[char] = 0
    template[char] += 1

tmp = {}
for char in s[:n]:
    if char not in tmp:
        tmp[char] = 0
    tmp[char] += 1

cnt = 1 if tmp == template else 0
for i in range(n, m):
    tmp[s[i - n]] -= 1
    if tmp[s[i - n]] == 0:
        del tmp[s[i - n]]

    if s[i] not in tmp:
        tmp[s[i]] = 0
    tmp[s[i]] += 1  
    
    if tmp == template:
        cnt += 1 

print(cnt)



