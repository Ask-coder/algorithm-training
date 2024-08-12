'''
Сайт посетило N человек, для каждого известно время входа на сайт In  и время выхода с сайта Out. 
Считается, что человек был на сайте с момента In по Out включительно. 

Определите, какое максимальное количество человек было на сайте одновременно.

Решение:
Создадим для каждого человека два события: вход и выход. Каждое событие - пара, 
в которой первое число - время, а второе - тип события.
Событие "вход на сайт" должно происходить раньше "выхода с сайта".
'''

def maxvisitorsonline(n, tin, tout):
    events = []
    for i in range(n):
        events.append((tin[i], -1))  
        events.append((tout[i], 1)) 
    events.sort()
    online = 0
    maxonline = 0
    for event in events:
        if event[1] == -1:
            online += 1
        else:
            online -= 1
        maxonline = max(online, maxonline)
    return maxonline
