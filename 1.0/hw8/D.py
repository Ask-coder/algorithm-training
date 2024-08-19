def insert(root, value):
    if value < root[2]:
        if root[0] is None:
            root[0] = [None, None, value]
        else:
            return insert(root[0], value)
    elif value > root[2]:
        if root[1] is None:
            root[1] = [None, None, value]
        else:
            return insert(root[1], value) 


def traverse(root):
    if root[0] is None and root[1] is None:
        print(root[2])
        return
    if root[0] is not None:
        traverse(root[0])
    print(root[2])
    if root[1] is not None: 
        traverse(root[1])
        


if __name__ == '__main__':
    arr = list(map(int, input().split()))
    
    tree = [None, None, None]
    if len(arr) > 1:
        tree[2] = arr[0]
    
    for i in range(1, len(arr)):
        if arr[i] == 0:
            break
        insert(tree, arr[i])

    traverse(tree)
