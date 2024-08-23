from collections import deque

def bfs(human, tree):
    cnt = 0
    queue = deque()
    visited = set()

    if human not in tree:
        return cnt
    queue = deque()
    queue.extend(tree[human])

    while queue:
        cnt += 1
        item = queue.popleft()
        visited.add(item)
        if item in tree:
            for i in tree[item]:
                if i not in visited:
                    queue.append(i)
                    visited.add(i) 
    return cnt


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
            
for human in sorted(humans):
    print(human, bfs(human, tree))

