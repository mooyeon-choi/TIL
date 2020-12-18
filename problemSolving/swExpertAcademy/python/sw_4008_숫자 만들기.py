def cal(idx, numsum):
    if idx == len(numbers):
        result.append(numsum)
        return
    for i in range(4):
        if sign[i]:
            if i == 0:
                sign[i] -= 1
                cal(idx + 1, numsum + numbers[idx])
                sign[i] += 1
            elif i == 1:
                sign[i] -= 1
                cal(idx + 1, numsum - numbers[idx])
                sign[i] += 1
            elif i == 2:
                sign[i] -= 1
                cal(idx + 1, numsum * numbers[idx])
                sign[i] += 1
            elif i == 3:
                sign[i] -= 1
                if numsum < 0:
                    cal(idx + 1, (numsum * (-1) // numbers[idx]) * (-1))
                else:
                    cal(idx + 1, numsum // numbers[idx])
                sign[i] += 1

for tc in range(1, int(input()) + 1):
    n = int(input())
    sign = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    result = []
    cal(1, numbers[0])
    print('#{} {}'.format(tc, max(result)-min(result)))
