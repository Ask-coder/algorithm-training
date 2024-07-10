a = int(input())
b = int(input())
c = int(input())

if c < 0:
    print('NO SOLUTION')
elif a + b == c ** 2 and 2 * a + b == c ** 2:
    print("MANY SOLUTIONS")
else:
    if a != 0:
        x = (c ** 2 - b) / a
        if (x - int(x)) > 0:
            print("NO SOLUTION")
        else: 
            print(int(x))
    else:
        print('NO SOLUTION')

