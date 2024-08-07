'''
Михаил читает лекции по алгоритмам. За кадром стоит доска размером W*H сантиметров. Михаилу нужно разместить на доске
N квадратных стикеров со шпаргалками, при этом длина стороны стикера в сантиметрах должна быть целым числом.

Определите максимальную длину стороны стикера, чтобы все стикеры поместились на доске

Решение:


'''

def checkstickers(size, params):
    n, w, h = params
    return (w // size) * (h // size) >= n


def rbinsearch(l, r, check, checkparams):
    while l != r:
        m = (l + r + 1) // 2
        if check(m, checkparams):
            l = m
        else:
            r = m - 1