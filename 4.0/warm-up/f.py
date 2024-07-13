#! /usr/bin/env python3
# -*- coding: utf-8 -*-


k = int(input())  # количество людей, которое вмещает лифт за одну поездку
n = int(input())  # количество этажей в здании

data = [int(input()) for _ in range(n)]
count = 0
leftSeatsInElev = 0
print("-" * 50)

for i in range(n - 1, -1, -1):
    if data[i] == 0:
        continue
    # Лифт на этаже
    # он может быть пустой или частично заполнен
    if data[i] > leftSeatsInElev:
        count += ((data[i] - leftSeatsInElev + k - 1) // k) * (i + 1) * 2
        leftSeatsInElev = k - (data[i] - leftSeatsInElev) % k or leftSeatsInElev
    else:
       leftSeatsInElev -= data[i]


print(count)
