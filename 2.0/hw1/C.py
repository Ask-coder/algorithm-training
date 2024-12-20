'''
Как известно, два наиболее распространённых формата записи даты — это европейский 
(сначала день, потом месяц, потом год) и американски (сначала месяц, потом день, потом год). 
Системный администратор поменял дату на одном из бэкапов и сейчас хочет вернуть дату обратно. 
Но он не проверил, в каком формате дата используется в системе. Может ли он обойтись без этой информации?
Иначе говоря, вам даётся запись некоторой корректной даты. Требуется выяснить,
однозначно ли по этой записи определяется дата даже без дополнительной информации о формате.

Первая строка входных данных содержит три целых числа — 
x,y и z (1≤x≤31,1≤y≤31,1970≤z≤2069). 
Гарантируется, что хотя бы в одном формате запись 
xyz задаёт корректную дату.

Выведите 1, если дата определяется однозначно, и 0 в противном случае.
'''

if __name__ == "__main__":
    x, y, z = map(int, input().split())

    def check(x: int, y: int) -> int:
        if x > 12 or y > 12:
            return 1
        elif x == y:
            return 1
        # if (1 <= x <= 12 and 1 <= y <= 31) or (1 <= x <= 31 and 1 <= y <= 12):
            # return 1
        return 0

    print(check(x, y))

    with open('test.txt', 'w') as file:
        for i in range(1, 13):
            for j in range(1, 32):
                file.write(f'{i}-{j}-{z} || {j}-{i}-{z} | {"YES" if check(i, j) else 'NO'} \n')