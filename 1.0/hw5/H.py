from collections import deque

n, k = map(int, input().split())
line = input()

counter = {}
left = 0
cnt = 0
res_pos = 0
for i in range(n):
    if line[i] not in counter:
        counter[line[i]] = 0

    if counter[line[i]] == k:
        while line[left] != line[i]:
            counter[line[left]] -= 1
            left += 1
        counter[line[left]] -= 1
        left += 1
    counter[line[i]] += 1
    if i - left + 1 > cnt:
        cnt = i - left + 1
        res_pos = left + 1

print(cnt, res_pos)