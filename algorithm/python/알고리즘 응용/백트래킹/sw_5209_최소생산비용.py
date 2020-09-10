def back(i, numsum):
    global answer
    if answer <= numsum:
        return
    if i == n:
        answer = numsum
        return
    for j in range(n):
        if not used[j]:
            used[j] = 1
            back(i + 1, numsum+fac[i][j])
            used[j] = 0

t = int(input())
for tc in range(1, t + 1):
    answer = 0xffffff
    n = int(input())
    fac = [list(map(int, input().split())) for _ in range(n)]
    used = [0]*n
    back(0, 0)
    print('#{} {}'.format(tc, answer))