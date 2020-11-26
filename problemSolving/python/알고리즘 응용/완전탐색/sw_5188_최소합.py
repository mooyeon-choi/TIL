def back(i, j, num):
    global min_num
    num += num_map[i][j]
    if i == n - 1 and j == n - 1:
        if min_num > num:
            min_num = num
    else:
        if i + 1 < n:
            back(i + 1, j, num)
        if j + 1 < n:
            back(i, j + 1, num)


t = int(input())
for tc in range(1, t + 1):
    min_num = 0xffffff
    n = int(input())
    num_map = [list(map(int, input().split())) for _ in range(n)]
    back(0,0,0)
    print('#{} {}'.format(tc, min_num))