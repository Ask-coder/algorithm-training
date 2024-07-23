nums1 = set(map(int, input().split()))
nums2 = set(map(int, input().split()))

print(*sorted(nums1.intersection(nums2)))