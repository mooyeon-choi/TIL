def dfs(m, num):
    global result
    num *= work[m][i]
    if num <= result:
        return
    for j in range(n):
        if not solve[j]:
            solve[j] = 1
            dfs(m+1, num)
            solve[j] = 0
    if m == n - 1:
        if num > result:
            result = num
        return


t = int(input())
for tc in range(1, t + 1):
    result = 0
    n = int(input())
    work = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            work[i][j] /= 100
    solve = [0]*n
    for i in range(n):
        solve[i] = 1
        dfs(0, 1)
        solve[i] = 0
    print('#{} {:.6f}'.format(tc, result*100))