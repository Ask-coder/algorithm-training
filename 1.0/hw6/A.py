n, k = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
arr1.sort()


def bin_serarch(arr, key):
    l = 0
    r = len(arr)

    while l < r:
        m = (l + r) // 2
        if arr[m] == key:
            return 'YES'        
        elif arr[m] > key:
            r = m
        else:
            l = m + 1
    return 'NO'

for i in range(k):
    print(bin_serarch(arr1, arr2[i]))