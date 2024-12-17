

def solution(n, k, a):
    a = sorted(a)
    if n == 1:
        return 1
    if n == 2:
        if a[1] - a[0] > k:
            return 1
        else:
            return 2
    
        
    l = r = 0
    cnt = 0
    
    while l < len(a):
        while r < len(a) and (l == r or abs(a[l] - a[r] <= k)):
            r += 1
        cnt += 1
        l = r
    
    return cnt

n, r = map(int, input().split())
arr = list(map(int, input().split()))
print(solution(n, r, arr))