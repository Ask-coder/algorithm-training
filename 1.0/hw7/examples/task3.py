'''
Сайт посетило N человек, для каждого известно время входа на сайт In и время выхода 
с сайта Out. Считается, что человек был на сайте с момента In по Out включительно.
Начальник заходил на сайт M раз с момента времени Boss и смотрел, сколько людей сейчас онлайн. 
Посещения сайта начальником упорядочены по возрастанию времени

Определите, какие показания счётчика людей онлайн увидел начальник.

Решение:
Создадим третий тип события - "вход начальника" и при наступлении такого события 
будем сохранять текущее значение счётчика посетителей
'''

def bosscounters(n, tin, tout, m, tboss):
    events = []
    for i in range(n):
        events.append((tin[i], -1))
        events.append((tout[i], 1))

    for i in range(m):
        events.append((tboss[i], 0))
    events.sort()
    online = 0
    bossans = []
    for i in range(len(events)):
        if events[i][1] == -1:
            online += 1
        elif events[i][1] == -1:
            online -= 1
        else:
            bossans.append(online)
    return bossans
