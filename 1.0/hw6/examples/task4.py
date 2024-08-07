'''
 Задана отсортированная по неубыванию последовательность из N числе и число X. 
 Необходимо определить индекс первого числа в последовательности, которое больше либо равно X. Если такого числа нет, то вернуть число N

 Решение:

 '''

def checkisge(index, params):
    seq, x = params
    return seq[index] >= x


def findfirstge(seq, x):
    ans = lbinsearch(0, len(seq) - 1, checkisge, (seq, x))
    if seq[ans] < x:
        return len(seq)
    return ans


def lbinsearch(l, r, check, checkparams):
    seq, x = checkparams
    while l < r:
        m = (l + r) // 2
        if check(m, checkparams):
            r = m
        else:
            l = m + 1