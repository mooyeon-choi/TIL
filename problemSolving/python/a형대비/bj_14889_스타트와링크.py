def counting(team, sl):
    global num
    if len(team) == 2:
        num += stats[team[0]][team[1]]
        return
    else:
        for i in range(len(sl)):
            if not visit[i]:
                team.append(sl[i])
                counting(team, sl)
                team.pop()



n = int(input())
stats = [list(map(int, input().split())) for _ in range(n)]
total = set([i for i in range(n)])
starts =[]
result = []
for i in range(1 << n):
    t = []
    for j in range(n):
        if i & (1 << j):
            t.append(j)
    if len(t) == n//2:
        starts.append(set(t))
for start in starts:
    link = total - start
    num = 0
    visit = [0]*len(start)
    counting([], list(start))
    st_num = num
    num = 0
    visit = [0] * len(link)
    counting([], list(link))
    li_num = num
    result.append(abs(st_num - li_num))
print(min(result))