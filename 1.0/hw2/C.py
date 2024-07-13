
def findx(arr, x):
    ans = arr[0]
    diff = abs(x - arr[0])
    for i in range(1, n):
        if abs(x - arr[i]) < diff:
            diff = abs(x - arr[i])
            ans = arr[i]
    return ans


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    x = int(input())
    print(findx(arr, x))

