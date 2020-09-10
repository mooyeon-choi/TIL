def back(string):
    global min_num
    if len(string) == n:
        string += '0'
        num_sum = 0
        for i in range(len(string) - 1):
            num_sum += e[int(string[int(i)])][int(string[int(i) + 1])]
        if min_num > num_sum:
            min_num = num_sum
        return

    for i in range(n):
        if not visit[i]:
            visit[i] = 1
            back(string + str(i))
            visit[i] = 0


t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    e = [list(map(int, input().split())) for _ in range(n)]
    visit = [1] + [0]*(n - 1)
    min_num = 0xffffff
    back('0')
    print('#{} {}'.format(tc, min_num))
