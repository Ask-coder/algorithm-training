
def find_two_min_max(arr):
    max_1, max_2 = max(arr[0], arr[1]), min(arr[0], arr[1])
    min_1, min_2 = min(arr[0], arr[1]), max(arr[0], arr[1])

    for i in range(2, len(arr)):
        if arr[i] >= max_1:
            max_2 = max_1
            max_1 = arr[i]
        elif arr[i] >= max_2:
            max_2 = arr[i]
        elif arr[i] <= min_1:
            min_2 = min_1
            min_1 = arr[i]
        elif arr[i] <= min_2:
            min_2 = arr[i]

    return (max_1, max_2, min_1, min_2)      


if __name__ == '__main__':
    arr = list(map(int, input().split()))
    max_1, max_2, min_1, min_2 = find_two_min_max(arr)

    if min_1 * min_2 >= max_1 * max_2:
        print(min_1, min_2)
    else:
        print(max_2, max_1)

