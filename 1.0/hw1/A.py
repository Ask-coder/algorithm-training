troom, tcond = map(int, input().split())
mode = input()

res = 0
if mode == 'freeze':
	if tcond > troom:
		res = troom
	else:
		res = tcond
elif mode == 'heat':
	if troom > tcond:
		res = troom
	else:
		res = tcond
elif mode == 'auto':
	res = tcond	
elif mode == 'fan':
	res = troom

print(res)

