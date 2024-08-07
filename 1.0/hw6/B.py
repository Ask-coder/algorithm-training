n, k = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))


def lbinsearch(arr: list, key: int) -> int:
    l = 0
    r = len(arr)

    while l < r:
        m = (l + r) // 2
        if key < arr[m]:
            r = m
        else:
            l = m + 1

    return l


def rbinsearch(arr: list, key: int) -> int:
    l = 0
    r = len(arr) - 1

    while l < r:
        m = (l + r + 1) // 2
        if key < arr[m]:
            r = m - 1
        else:
            l = m

    return l


for i in range(k):
    l = lbinsearch(x, y[i])
    r = rbinsearch(x, y[i])

    if l >= n:
        l = n - 1

    if r >= n:
        r = n - 1
   
    if l == r:
        print(x[r])
    elif abs(x[l] - y[i]) > abs(x[r] - y[i]):
        print(x[r])
    elif abs(x[l] - y[i]) == abs(x[r] - y[i]):
        print(min(x[l], x[r]))
    else:
        print(x[l])



        