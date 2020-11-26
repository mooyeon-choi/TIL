t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    numbers = list(map(int, input().split()))
    number = set([0])
    for i in range(n):
        num = set()
        for j in number:
            num.add(j+numbers[i])
        number = number | num
    print(number)
    print('#{} {}'.format(tc, len(number)))