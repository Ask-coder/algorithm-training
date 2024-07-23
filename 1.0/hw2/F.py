def is_palindrom(arr, l):
    r = len(arr) - 1
    while l < r:
        if arr[l] != arr[r]:
            return False
        l += 1
        r -= 1
    return True

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    ans = []
    for i in range(len(arr)):        
        if is_palindrom(arr, i):
            break
        else:
            ans.append(arr[i])

    print(len(ans))
    if len(ans) > 0:
        ans.reverse()
        print(' '.join(list(map(str, ans))))
