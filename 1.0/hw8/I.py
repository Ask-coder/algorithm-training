
import sys

sys.setrecursionlimit(100000)


if __name__ == '__main__':
    n = int(input())
    humans = set()
    tree = dict()
    for _ in range(n - 1):
        child, parent = input().split()
        humans.add(child)
        humans.add(parent)
        
        if parent not in tree:
            tree[parent] = set()
        tree[parent].add(child)            


res = {}
def count(human, root):
    if human in res:
        return res[human] 

    if human not in root:
        return 0
    
    cnt = len(root[human])
    for item in root[human]:
        cnt += count(item, root)
    return cnt


for human in humans:
    res[human] = count(human, tree)    


for key in sorted(res.keys()):
    print(key, res[key])




