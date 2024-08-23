def insert(root, value):
    if value < root[2]:
        if root[0] is None:
            root[0] = [None, None, value]
        else:
            insert(root[0], value)
    elif value > root[2]:
        if root[1] is None:
            root[1] = [None, None, value]
        else:
            insert(root[1], value)


def get_height(root, ans):
    if root is None:
        return 0
    h_l = get_height(root[0], ans)
    h_r = get_height(root[1], ans)
    ans.append(abs(h_l - h_r) < 2) 
    return max(h_l, h_r) + 1


if __name__ == '__main__':
    nums = list(map(int, input().split()))

    tree = [None, None, None]
    for num in nums:
        if num == 0: 
            break

        if tree[2] is None:
            tree[2] = num
        else:
            insert(tree, num)

    ans = []
    get_height(tree, ans)
    print('YES' if all(ans) else 'NO')