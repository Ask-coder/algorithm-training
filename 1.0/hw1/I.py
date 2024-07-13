A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

# 1st case
if (D >= A and E >= B) or (D >= B and E >= A):
    print('YES')
elif (D >= A and E >= C) or (D >= C and E >= A):
    print('YES')
elif (D >= B and E >= C ) or (D >= C and E >= B):
    print('YES')
else:
    print('NO')