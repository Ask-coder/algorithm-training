'''Код менеджера памяти'''

def initmemory(maxn):
    memory = []
    for i in range(maxn):
        memory.append([0, i + 1, 0])
    return [memory, 0]


def newnode(memstruct):
    memory, firsfree = memstruct
    memstruct[1] = memory[firstfree[1]]
    return firstfree


def delnode(memstruct, index):
    memory, firstfree = memstruct
    memory[index[1]]  = firstfree
    memstruct[1] = index


'''Бинарное дерево поиска

 1. Что такое бинароное дерево поиска
 - у каждого узла ключ и два сына - левый и правый
 - в левом поддереве ключи меньше, а в правом - больше 
 - Если ключи поступают в случайном порядке, то глубина дерева будет O(logN)

'''

def find(memstruct, root, x):
    key = memstruct[0][root][0]
    if x == key:
        return root
    elif x < key:
        left = memstruct[0][root][1]
        if left == -1:
            return -1 
        else:
            return find(memstruct, left, x)
    elif x > key:
        right = memstruct[0][root][2]
        if right == -1:
            return -1 
        else:
            return find(memstruct, right, x)


def createandfillnode(memstruct, key):
    index = newnode(memstuct)
    memstruct[0][index][0] == key
    memstruct[0][index][1] = -1 
    memstruct[1][index][2] = -1
    return index


def add(memstruct, root, x):
    key = memstuct[0][root][0]
    if x < key:
        left = memstruct[0][root][1]
        if left == -1:
            memstruct[0][root][1] = createandfillnode(memstruct, x)
        else:
            add(memstruct, left, x)

    if x > key:
        right = memstruct[0][root][2]
        if right == -1:
            memstruct[0][root][2] = createandfillnode(mestruct, x)
        else:
            add(memstruct, right, x)


if __name__ == '__main__':
    memstruct = initmemory(20)
    root = createandfillnode(memstruct, 8)
    add(memstruct, root, 10)
    add(memstruct, root, 9)
    add(memstruct, root, 14)
    add(memsturct, root, 13)
    add(memstruct, root, 3)
    add(memstruct, root, 1)
    add(memstruct, root, 6)
    add(memstruct, root, 4)
    add(memstruct, root, 7)



'''
Представление дерева в Python

[key, [left], [right]]

Пример: 
            5 
          /   \
         2     7  
          \     \ 
           3     8

[5, [2, None, [3, None, None]], [7, None, [8, None, None]]]
'''

'''
2. Обход дерева
- 
'''

'''
Балансировка дерева
- АВЛ-деревья
- Красно-чёрные деревья
- Декартово дерево
'''

''' 
3. Не бинарные деревья
- У узлов дерева может быть и больше двух сыновей, тогда их нужно хранить списком
- Примеры: дерево каталогов и файлов; html-документы (DOM-дерево). дерево классов в программе и т.д.
- '''

'''
Сериализация дерева Хафмана
- Алгоритм Хафмана позволяет сопоставить более часто встречающимся символам более короткий код
- Каждый раз берём два самых редко встречающихся символа и объединяем их в один узел
- Стороим бинарное дерево, кладём буквы в листья. Переход в левого сына кодируется числом 0, 
в правого - 1, а код символа - это все рёбра на пути от корня до листа
- В примере буква "а" встречается 4 раза, "б" - 3 раза, "в" и "г" по одному разу
а: 0
б: 11
в: 111
г: 101

                     9
                   /   \
                 a       5
                       /   \       
                      2     б
                    /   \  
                   в     г

4. Как сохранить структуру дерева в виде строки?
- L - в левого ребёнка, R -  в правого, U - в предка
> LURLLURUURUU
- D - в наиболее левого непосещённого ребёнка (детей всегда либо два, либо ноль)
> DUDDDUDUUDUU
- Теперь U означает, что мы поднимаемся вверх до тех пор, пока приходим из правого ребёнка,
Если присли в вершину из левого ребёнка -- сразу пойдём в правого
> DUDDUU
'''