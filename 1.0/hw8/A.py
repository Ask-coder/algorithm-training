'''
Реализовать бинарное дерево поиска для целых чисел. Программа получает на вход последовательность 
целых чисел и строит из них дерево. Элементы в деревья добавляются в соответствии с результатом 
поиска их места. Если элемент уже существует в дереве, добавлять его не надо. 
Балансировка дерева не производится.

На вход программа получает последовательность натуральных чисел. Последовательность завершается числом 0, 
которое означает конец ввода, и добавлять его в дерево не надо. 
'''

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class BTree:
    def __init__(self):
        self.root = None
        self.h = 0
    
    def height(self):
        def _height(node):
            if node is None:
                return 0

            l = _height(node.left)
            r = _height(node.right)
            h = max(l, r)
            return  h + 1
        return _height(self.root)
    

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
            self.h = 1
        else:
            h = self._insert_recursively(self.root, key, 2)
            self.h = max(h, self.h)

    def _insert_recursively(self, node, key, height):
        if key < node.value:
            if node.left is None:
                node.left = Node(key)
            else:
                return self._insert_recursively(node.left, key, height + 1)
        elif key > node.value:
            if node.right is None:
                node.right = Node(key)
            else:
                return self._insert_recursively(node.right, key, height + 1)
        return height - 1



if __name__ == '__main__':
    lst = list(map(int, input().split()))
    tree = BTree()
    for i in range(len(lst)):
        if lst[i] != 0:
            tree.insert(lst[i])
        else:
            break

    print(tree.height())
    print(tree.h)


        