N, K, M = map(int, input().split())

cnt = 0
if N >= K >= M:
    cnt_detail_from_blank = K // M
    while N >= K:
        cnt_blank = N // K
        remainder = N % K
        cnt += cnt_detail_from_blank * cnt_blank
        remainder += (K % (cnt_detail_from_blank * M)) * cnt_blank
        N = remainder

print(cnt) 
    