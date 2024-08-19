
def insert(key, tree, height):
    if key < tree[0]:
        if tree[1] is None:
            tree[1] = [key, None, None]
        else:
            return insert(key, tree[1], height + 1)
    elif key > tree[0]:
        if tree[2] is None:
            tree[2] = [key, None, None]
        else:
            return insert(key, tree[2], height + 1)
    elif key == tree[0]:
        height -= 1
    return height


if __name__ == '__main__':
    lst = list(map(int, input().split()))
    tree = [None, None, None]
    h = 0
    for i in range(len(lst)):
        if lst[i] != 0:
            if tree[0] is None:
                tree[0] = lst[i]
                h = 1
            else:
                tmp = insert(lst[i], tree, 2)
                h = max(tmp, h)

    print(h)