lst = list(map(int, input().split()))

def find_three_min_max(lst):
    max_1, max_2, max_3 = sorted([lst[0], lst[1], lst[2]], reverse=True)
    min_1, min_2, min_3 = sorted([lst[0], lst[1], lst[2]])

    for i in range(3, len(lst)):
        if lst[i] >= max_1:
            max_3 = max_2
            max_2 = max_1
            max_1 = lst[i]
        elif lst[i] >= max_2:
            max_3 = max_2
            max_2 = lst[i]
        elif lst[i] >= max_3:
            max_3 = lst[i]

        elif lst[i] <= min_1:
            min_3 = min_2
            min_2 = min_1
            min_1 = lst[i]
        elif lst[i] <= min_2:
            min_3 = min_2
            min_2 = lst[i]
        elif lst[i] <= min_3:
            min_3 = lst[i]

    return [min_1, min_2, min_3, max_3, max_2, max_1]


res = find_three_min_max(lst)
prod_1 = res[3] * res[4] * res[5]
prod_2 = res[0] * res[1] * res[5]

if prod_1 > prod_2:
    print(res[3], res[4], res[5])
else:
    print(res[0], res[1], res[5])
