def dfs(i, j, count, num):
    global answer, anum
    for k in range(4):
        if 0 <= i + x[k] < n and 0 <= j + y[k] < n:
            if rooms[i + x[k]][j + y[k]] - rooms[i][j] == 1:
                dfs(i + x[k], j + y[k], count + 1, num)
    else:
        if count > answer:
            answer = count
            anum = num
        elif count == answer:
            if anum > num:
                anum = num
        return

x = [-1, 1, 0, 0]
y = [0, 0, -1, 1]
t = int(input())
for tc in range(1, t + 1):
    answer = 0
    anum = 0
    n = int(input())
    rooms = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            dfs(i, j, 1, rooms[i][j])
    print('#{} {} {}'.format(tc, anum, answer))