'''
Задача 2
Сайт посетило N человек, для каждого известно время входа на сайт In и время выхода с сайта Out. 
Считается, что человек был на сайте с момента In по Out включительно

Определите, какое суммарное время на сайте был хотя бы один человек.

Решение:
Если мы пришли в событие с положительным счётчиком количества людей, то между этим и 
предыдущим событием на сайте кто-то был. Прибавим к ответу время между текущим и предыдущим событием 
'''

def timewithvisitors(n, tin, tout):
    events = []
    for i in range(n):
        events.append((tin[i], -1))
        events.append((tout[i], 1))
    events.sort()

    online = 0
    notemptytime = 0
    for i in range(len(events)):
        if online > 0:
            notemptytime += events[i][0] - events[i - 1][0]
            if events[i][1] == -1:
                online += 1
            else:
                online -= 1
    return notemptytime