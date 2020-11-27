n = int(input())
for _ in range(n):
    num = int(input())
    nums = list(range(1, num + 1))
    if len(nums) % 2:
        nums[0], nums[len(nums) // 2] = nums[len(nums) // 2], nums[0]
        nums.reverse()
    else:
        nums.reverse()

    print(' '.join(map(str, nums)))