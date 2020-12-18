r, c, t = map(int, input().split())
dust = [list(map(int, input().split())) for _ in range(r)]
for i in range(r):
    for j in range(c):
        if dust[i][j] == -1:
            top = dust[:i]
            bot = dust[i:]
for t in top:
    print(t)
for b in bot:
    print(b)