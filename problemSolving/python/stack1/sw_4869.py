def cal(n):
    if n == 10:
        return 1
    elif n == 20:
        return 3
    return cal(n - 20) * 4 + 1

t = int(input())
for tc in range(t + 1):
    n = int(input())
    result = cal(n)
    print(result)