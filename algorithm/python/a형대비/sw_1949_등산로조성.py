def dfs(i, j, count, number):
    global answer, used
    if answer < count:
        answer = count
    for a in range(4):
        if 0 <= i+x[a] < n and 0 <= j+y[a] < n:
            if not visit[i+x[a]][j+y[a]] and mtn[i+x[a]][j+y[a]] < number:
                visit[i + x[a]][j + y[a]] = 1
                dfs(i+x[a], j+y[a], count + 1, mtn[i+x[a]][j+y[a]])
                visit[i + x[a]][j + y[a]] = 0
            elif not visit[i+x[a]][j+y[a]] and not used and mtn[i+x[a]][j+y[a]] - k < number:
                visit[i + x[a]][j + y[a]] = 1
                used = True
                dfs(i + x[a], j + y[a], count + 1, number - 1)
                visit[i + x[a]][j + y[a]] = 0
                used = False
    else:
        return


x = [-1, 1, 0, 0]
y = [0, 0, -1, 1]
t = int(input())
for tc in range(1, t + 1):
    answer = 0
    n, k = map(int, input().split())
    mtn = [list(map(int, input().split())) for _ in range(n)]
    max_num = max(map(max, mtn))
    for i in range(n):
        for j in range(n):
            if mtn[i][j] == max_num:
                used = False
                visit = [[0]*n for _ in range(n)]
                visit[i][j] = 1
                dfs(i, j, 1, max_num)
    print('#{} {}'.format(tc, answer))