def func(x1, y1, x2, y2, x, y):
    print(f'{x1=} {y1=} {x2=} {y2=} {x=} {y=}')
    # print( x <= x1 and y2 >= y)
    # print(f'{x} < {x1} {x < x1 =}')
    # print(f'{(y2 >= y)=}')
    
    if x <= x1 and y >= y2:
        return 'NW'
    if x <= x1 and y1 <= y <= y2:
        return 'W'
    if x <= x1 and y <= y1:
        return 'SW'
    if x1 <= x <= x2 and y <= y1:
        return 'S'
    if x >= x2 and y <= y1:
        return 'SE'
    if x >= x2 and y1 <= y <= y2:
        return 'E'
    if x >= x2 and y >= y2:
        return 'NE' 
    if x1 <= x <= x2 and y > y2:
        return 'N'


x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x = int(input())
y = int(input())

print(func(x1, y1, x2, y2, x, y))


print('NW', func(x1, y1 ,x2, y2, -2 , 4) == 'NW')
print('W', func(x1, y1 ,x2, y2, -8, 2) == 'W')
print('SW', func(x1, y1 ,x2, y2, -6, -4) == 'SW')
print('S', func(x1, y1 ,x2, y2, 2, -3) == 'S')
print('SE', func(x1, y1 ,x2, y2, 7, -3) == 'SE')
print('E', func(x1, y1 ,x2, y2, 12, 0) == 'E')
print('NE', func(x1, y1 ,x2, y2, 9, 4) == 'NE')
print('N', func(x1, y1 ,x2, y2, 3, 4) == 'N')