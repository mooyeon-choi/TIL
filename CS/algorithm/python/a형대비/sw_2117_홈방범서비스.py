def cal():
    for ground in range(n + 1, 0, -1):
        # 전체 좌표에서
        maxnum = 0
        for i in range(n):
            for j in range(n):
                # 마름모꼴 안에 들어오는 집이 몇개인지
                # 위로는 i - ground + 1, 아래로는 i + ground - 1
                homes = 0
                for u in range(i - ground + 1, i + ground):
                    # i 와 한칸 멀어질때마다 좌우 하나씩 줄어듦
                    for v in range(j - ground + abs(u - i) + 1, j + ground - abs(u - i)):
                        if 0 <= u < n and 0 <= v < n and board[u][v]:
                            homes += 1
                if homes > maxnum:
                    maxnum = homes
        if maxnum * m >= width[ground - 1]:
            return maxnum

for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    # 가장 큰 영역부터 돌면서
    width = []
    for i in range(n+1):
        if not i:
            width.append(1)
        else:
            width.append(width[i-1]+4*i)
    answer = cal()
    print('#{} {}'.format(tc, answer))