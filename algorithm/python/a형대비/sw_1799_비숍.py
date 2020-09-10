n = int(input())
chess = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(n):
        