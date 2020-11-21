def MergeSort(number):
    global answer
    left = number[:len(number)//2]
    right = number[len(number)//2:]
    if left and right:
        if max(left) > max(right):
            answer += 1
    else:
        return
    MergeSort(left)
    MergeSort(right)

t = int(input())
for tc in range(1, t + 1):
    answer = 0
    n = int(input())
    numbers = list(map(int, input().split()))
    MergeSort(numbers)
    numbers.sort()
    print('#{} {} {}'.format(tc, numbers[len(numbers)//2], answer))
