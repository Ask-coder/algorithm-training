a1, b1, a2, b2 = map(int, input().split())

a_new_1 = a1 + a2
b_new_1 = max(b1, b2)

a_new_2 = max(a1, a2)
b_new_2 = b1 + b2

a_new_3 = a1 + b2
b_new_3 = max(b1, a2)

a_new_4 = a2 + b1
b_new_4 = max(a1, b2)

res_1 = (a_new_1, b_new_1)
res_2 = (a_new_2, b_new_2)
res_3 = (a_new_3, b_new_3)
res_4 = (a_new_4, b_new_4)

res = min(res_1, res_2, res_3, res_4, key=lambda x: x[0] * x[1])
print(*res)

