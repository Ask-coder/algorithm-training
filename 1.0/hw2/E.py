n = int(input())
arr = list(map(int, input().split()))

def calc_place(arr):
    res = 0
    if len(arr) < 3:
        return res
    
    is_find = False
    idx = -1
    ans = 0
    my_max =  max(arr)
    for i in range(len(arr) - 1):
        if arr[i] == my_max and is_find == False:
            is_find = True
        elif is_find and arr[i] % 10 == 5 and arr[i] > arr[i + 1] and arr[i] > ans:
            ans = arr[i]
            idx = i

    if idx != -1:
        res = 1
        for i in range(len(arr)):
            if arr[i] > arr[idx]:
                res += 1   

    return res

print(calc_place(arr))


