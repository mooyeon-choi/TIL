def dfs(now, num):
    global answer
    if num > answer:
        return
    if all(visit):
        num += abs(now[0] - end[0]) + abs(now[1] - end[1])
        if num < answer:
            answer = num
        return
    for i in range(n):
        if not visit[i]:
            visit[i] = 1
            dfs(homes[i], num + abs(now[0] - homes[i][0]) + abs(now[1] - homes[i][1]))
            visit[i] = 0


t = int(input())
for tc in range(1, t + 1):
    answer = 400
    n = int(input())
    visit = list(map(int, input().split()))
    homes = []
    for i in range(0, len(visit), 2):
        if not i:
            start = (visit[i], visit[i + 1])
        elif i == 2:
            end = (visit[i], visit[i + 1])
        else:
            homes.append((visit[i], visit[i + 1]))
    visit = [0]*n
    dfs(start, 0)
    print('#{} {}'.format(tc, answer))