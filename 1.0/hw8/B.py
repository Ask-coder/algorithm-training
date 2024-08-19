def insert(key, tree, hs):
    if key < tree[0]:
        if tree[2] is None:
            tree[2] = [key, tree[1] + 1, None, None]
            hs.append(tree[2][1])
        else:
            insert(key, tree[2], hs)
    elif key > tree[0]: 
        if tree[3] is None:
            tree[3] = [key, tree[1] + 1, None, None]
            hs.append(tree[3][1])
        else:
            insert(key, tree[3], hs)
    return hs


if __name__ == '__main__':
    lst = list(map(int, input().split()))
    tree = [None, 0, None, None]
    
    hs = []
    for i in range(len(lst)):
        if lst[i] == 0:
            break

        if tree[0] is None:
            tree[0] = lst[i]
            tree[1] = 1
            hs.append(1)
        else:
            insert(lst[i], tree, hs)
    
    print(*hs)