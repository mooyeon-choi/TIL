def dfs(i, j, visit, num):
    global answer
    if len(visit) == n+1:
        answer += num
        return
    for k in range(4):
        if d[k][2]:
            if (i+d[k][0], j+d[k][1]) not in visit:
                visit.append((i+d[k][0], j+d[k][1]))
                dfs(i+d[k][0], j+d[k][1], visit, num*d[k][2])
                visit.pop()


n, E, W, S, N = map(int, input().split())
answer = float(0)
d = [(-1, 0, N/100), (0, 1, E/100), (1, 0, S/100), (0, -1, W/100)]
dfs(0, 0, [(0, 0)], 1)
print(answer)
