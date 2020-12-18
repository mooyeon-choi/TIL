from collections import deque

x = [0, 0, -1, 1]
y = [-1, 1, 0, 0]
def solution(maps):
    answer = 1
    que = deque([(0, 0)])
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j]: maps[i][j] = 0xfffffff
    while que:
        for _ in range(len(que)):
            i, j = que.popleft()
            maps[i][j] = 0
            if (i, j) == (len(maps) - 1, len(maps[0]) - 1):
                return answer
            for k in range(4):
                if 0 <= i+x[k] < len(maps) and 0 <= j+y[k] < len(maps[0]) and maps[i+x[k]][j+y[k]] > answer:
                    maps[i+x[k]][j+y[k]] = answer
                    que.append((i+x[k], j+y[k]))
        answer += 1
    return -1