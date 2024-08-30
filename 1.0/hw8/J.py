n = int(input())

tree = {}
humans = set()
for i in range(n - 1):
    child, parent = input().split()
    humans.add(child)
    humans.add(parent)
    tree[child] = parent

res = {}
def height(root, human):
    if human in root:
        return 1 + height(root, root[human])
    else:
        return 0

for human in humans:
    res[human] = height(tree, human)

for key in sorted(res.keys()):
    print(key, res[key])