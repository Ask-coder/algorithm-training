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


def traverse(root, h_l, h_r):
    if root is None:
        return 
    h_l += traverse(root[0], h)
    print(root[2], h_l, h_r)
    h_r += traverse(root[1], h)


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

    traverse(tree)