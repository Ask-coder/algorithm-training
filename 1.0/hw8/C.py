def insert(key, root):
    if key < root[0]:
        if root[1] is None:
            root[1] = [key, None, None, root[0]]
        else:
            insert(key, root[1])
    if key > root[0]:
        if root[2] is None:
            root[2] = [key, None, None, root[0]]
        else:
            insert(key, root[2])


def find_first_max(root):
    if root[2] is None:
        return root
    return find_first_max(root[2])


if __name__ == '__main__':
    lst = list(map(int, input().split()))
    tree = [None, None, None, None]
    
    for i in range(len(lst)):
        if lst[i] == 0:
            break

        if tree[0] is None:
            tree[0] = lst[i]
        else:
            insert(lst[i], tree)

    firstmax = find_first_max(tree)
    print(firstmax)
    print(firstmax[3] if firstmax[1]is None else find_first_max(firstmax[1])[0])
            

