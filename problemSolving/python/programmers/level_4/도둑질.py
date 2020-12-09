def solution(money):
    memo = [0]*(len(money) - 1)
    memo[0] = money[0]
    for i in range(1, len(money) - 1):
        if i == 1:
            memo[i] = money[i]
        elif i == 2:
            memo[i] = memo[0] + money[i]
        else:
            memo[i] = max(memo[i - 2], memo[i - 3]) + money[i]
    memo1 = [0]*(len(money))
    for i in range(1, len(money)):
        if i == 1:
            memo1[i] = money[i]
        elif i == 2:
            memo1[i] = money[i]
        else:
            memo1[i] = max(memo1[i - 2], memo1[i - 3]) + money[i]
    answer = max(memo[-1], memo[-2], memo1[-1], memo1[-2])
    return answer