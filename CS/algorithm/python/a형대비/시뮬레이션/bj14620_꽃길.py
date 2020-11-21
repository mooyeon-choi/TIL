def back(numsum, cnt):
    global answer
    if cnt == 3 or numsum > answer:
        if numsum < answer:
            answer = numsum
        return
    for i in range(1, N - 1):
        for j in range(1, N - 1):
            if not visit[i][j]:
                num = 0
                for k in range(5):
                    num += board[i+dirs[k][0]][j+dirs[k][1]]
                    visit[i+dirs[k][0]][j+dirs[k][1]] += 1
                for k in range(8):
                    if 0 <= i+used[k][0] < N and 0 <= j+used[k][1] < N:
                        visit[i+used[k][0]][j+used[k][1]] += 1
                back(numsum + num, cnt + 1)
                for k in range(5):
                    visit[i+dirs[k][0]][j+dirs[k][1]] -= 1
                for k in range(8):
                    if 0 < i+used[k][0] < N and 0 < j+used[k][1] < N:
                        visit[i+used[k][0]][j+used[k][1]] -= 1


used = [(-2, 0), (-1, -1), (-1, 1), (0, -2), (0, 2), (1, -1), (1, 1), (2, 0)]
dirs = [(-1, 0), (1, 0), (0, 1), (0, -1), (0, 0)]
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
visit = [[0]*N for _ in range(N)]
answer = 9999
back(0, 0)

print(answer)

