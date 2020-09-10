n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]
chicken = []
for i in range(n):
    for j in range(n):
        if city[i][j] == 2:
            chicken.append((i, j))

can = []
for i in range(1<<len(chicken)):
    chic = []
    for j in range(len(chicken)):
        if i & (1<<j):
            chic.append(chicken[j])
    if len(chic) == m:
        can.append(chic)

num_sum = [0]*len(can)
for c in range(len(can)):
    for i in range(n):
        for j in range(n):
            if city[i][j] == 1:
                num = []
                for chick in can[c]:
                    num.append(abs(i-chick[0]) + abs(j-chick[1]))
                num_sum[c] += min(num)
print(min(num_sum))