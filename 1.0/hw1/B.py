a = int(input())
b = int(input())
c = int(input())

ans = 'NO'
if (a + b > c and a + c > b and b + c > a): 
    ans = 'YES'

print(ans)