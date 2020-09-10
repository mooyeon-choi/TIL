def back(value, count):
    global answer
    if value == 1:
        if answer > count:
            answer = count
        return
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] <= value and nums[i] > 1:
            if not value % nums[i]:
                back(value // nums[i], count + 1 + len(str(nums[i])))

t = int(input())
for tc in range(1, t + 1):
    answer = 0xffffff
    numbers = list(map(int, input().split()))
    goal = int(input())
    nums = []
    for i in range(goal//2 + 1):
        for j in range(len(str(i))):
            if not numbers[int(str(i)[j])]:
                break
        else:
            if i > 1:
                if not goal % i:
                    nums.append(i)
    for i in range(len(str(goal))):
        if not numbers[int(str(goal)[i])]:
            break
    else:
        answer = len(str(goal)) + 1
    if answer == 0xffffff:
        back(goal, 0)
    if answer == 0xffffff:
        answer = -1
    print('#{} {}'.format(tc, answer))