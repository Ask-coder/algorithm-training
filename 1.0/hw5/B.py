n, k = map(int, input().split())
nums = list(map(int, input().split()))

prefix = [0] * (n + 1)
for i in range(n):
    prefix[i + 1] = prefix[i] + nums[i]

l = r = 0
cnt = 0
while r < n + 1:
    tmp = prefix[r] - prefix[l]
    if tmp > k:
        l += 1
    elif tmp < k:
        r += 1
    else:
        cnt += 1
        l += 1
        r += 1


print(cnt)
