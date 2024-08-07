'''
Задана отсортированная по неубыванию последовательность из N чисел и число X

Необходимо определить сколько раз число X входит в последовательность

Решение:
Найдем одним левым бинпоиском первое число больше либо равное X, а вторым левым бинпоиском - число строго большее X. 
Разность индексов и будет будет количеством вхождений
'''

def checkisgt(index, params):
    seq, x = params
    return seq[index] > x


def checkisgte(index, params):
    seq, x = params
    return seq[index] >= x


def findfirst(seq, x, check):
    ans = lbinsearch(0, len(seq) - 1, check, (seq, x))
    if not check(ans, (seq, x)):
        return len(seq)
    return ans

def countx(seq, x):
    indexgt = findfirst(seq, x, checkisgt)
    indexgte = findfirst(seq, x, checkisgte)
    return indexgt - indexgte

def lbinsearch(l, r, check, checkparams):
    while l < r:
        m = (l + r) // 2
        if check(m, checkparams):
            r = m
        else:
            l = m + 1