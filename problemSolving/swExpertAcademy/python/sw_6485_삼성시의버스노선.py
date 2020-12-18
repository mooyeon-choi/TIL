t = int(input())
for tc in range(1, t + 1):
    print('#{}'.format(tc), end='')
    n = int(input())
    count = [0]*5001
    for _ in range(n):
        a, b = map(int, input().split())
        for i in range(a, b + 1):
            count[i] += 1
    p = int(input())
    for i in range(p):
        if i == p - 1:
            print('', count[int(input())])
        else:
            print('', count[int(input())], end='')
