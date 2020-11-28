n = int(input())
for _ in range(n):
    c = int(input())
    nums = list(map(int, input().split()))
    numSet = set()
    removeSet = set()
    for num in nums:
        if num not in numSet:
            if num not in removeSet:
                numSet.add(num)
        else:
            numSet.remove(num)
            removeSet.add(num)
    if numSet:
        minNum = min(numSet)
        for i in range(len(nums)):
            if nums[i] == minNum:
                print(i + 1)
                break
    else:
        print(-1)