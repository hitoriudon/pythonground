import heapq
n = int(input())
i = int(input())
coms = []
for _ in range(i):
    nums= list(map(int, input().split()))
    for k in range (len(coms)):
        if nums[0] not in coms and nums[1] not in coms:
            coms.append(nums)
print(coms)