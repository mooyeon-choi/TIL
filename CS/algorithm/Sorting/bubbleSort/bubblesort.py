inputs = [3, 1, 7, 9, 2, 6]

def BubbleSort(nums):
    lastIdx = len(nums) - 1
    for cnt in range(lastIdx):
        for idx in range(lastIdx - cnt):
            if nums[idx] > nums[idx + 1]:
                nums[idx], nums[idx + 1] = nums[idx + 1], nums[idx]

    return nums

print(BubbleSort(inputs))