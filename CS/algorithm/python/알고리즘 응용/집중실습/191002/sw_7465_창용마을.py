def dfs(i):
    used[i] = 1
    for j in Q[i]:
        if not used[j]:
            dfs(j)
    else:
        return


t = int(input())
for tc in range(1, t + 1):
    answer = 0
    n, m = map(int, input().split())
    known = [list(map(int, input().split())) for _ in range(m)]
    Q = [[] for _ in range(n + 1)]
    used = [1] + [0]*n
    for i in range(m):
        Q[known[i][0]].append(known[i][1])
        Q[known[i][1]].append(known[i][0])
    for i in range(1, n + 1):
        if not used[i]:
            dfs(i)
            answer += 1
    print('#{} {}'.format(tc, answer))