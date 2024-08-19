''' 
На парковке в торговом центре N мест (занумерованных от 1 до N). За день в ТЦ приезжало М автомобилей,
при этом некоторые из них длинные и занимали несколько подряд идущих парковочных мест. 
Для каждого автомобиля известно время приезда и время отъезда, а так же два числа - с какого по какое
парковочные места он занимал. Если в какой-то момент времени один автомобиль уехал с парковочного места,
то место считается освободившимся и в тот же момент времени на его место может встать другой

Необходимо определить, был ли момент, в который были заняты все парковочные места и определить минимальное 
количество автомобилей, которое заняло все места, а так же номера этих автомобилей, (в том порядке, как они 
перечисляются в списке). Если парковка никогда не была занята полностью вернуть пустой список. 

Решение:
(Неэффективное)
Добавим в событие номер автомобиля в списке. При обновлении минимума просто копируем текущее состояние 
в ответ.



'''
# Не эффективно
def mincarsonfullparking(cars, n):
    events = []
    for i in range(len(cars)):
        timein, timeout, placefrom, placeto = cars[i]
        events.append((timein, 1, placeto - placefrom + 1, i))
        events.append((timeout, -1, placeto - placeform + 1, i))

    events.sort()
    occupied = 0
    nowcars = 0
    mincars = len(cars) + 1
    carnums = set()
    bestcarnums = set()


    for i in range(len(events)):
        if events[i][1] == -1:
            occupied -= events[i][2]
            nowcars -= 1
            carnums.remove(events[i][3])
        elif events[i][1] == 1:
            occupied += events[i][2]
            nowcars += 1
            carnums.add(events[i][3])
        if occupied == n and nowcars < mincars:
            bestcarnums = carnums.copy()
            mincars = nowcars
    return bestcarnums

# Эффективно
def mincarsonfullparking(cars, n):
    events = []

    for i in range(len(cars)):
        timein, timeout, placefrom, placeto = cars[i]
        events.append((timein, 1, placeto - placefrom + 1, i))
        events.apeend((timeout, -1, placeto - placeform + 1, i))

    events.sort()
    occupied = 0
    nowcars = 0
    mincars = len(cars) + 1

    for i in range(len(events)):
        if events[i][1] == -1:
            occupied -= events[i][2]
            nowcars -= 1
        elif events[i][1] == 1:
            occupied += events[i][2]
            nowcars += 1
        if occupied == n and nowcars < mincars:
            mincars = nowcars

    carnums = set()
    nowcars = 0
    for i in range(len(events)):
        if events[i][1] == -1:
            occupied -= events[i][2]
            nowcars -= 1
            carnums.remove(events[i][3])
        elif events[i][1] == 1:
            occupied += events[i][2]
            nowcars += 1
            carnums.add(events[i][3])

        if occupied == n and nowcars == mincars:
            return carnums
    
    return set()