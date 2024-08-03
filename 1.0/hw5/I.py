k = int(input())
line = input()
cnt = 0
left = 0
prev_len = 0 

for i in range(k, len(line)):
    if line[i] == line[i - k]:
        prev_len += 1
        cnt += prev_len
    else:
        prev_len = 0

print(cnt)

