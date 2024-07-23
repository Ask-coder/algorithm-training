x, y, z = map(int, input().split())
n = int(input())

nums = set()

while n > 0:
    nums.add(n % 10)
    n //= 10

print(len(nums.difference({x, y, z})))