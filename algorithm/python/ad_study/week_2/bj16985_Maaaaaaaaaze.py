import collections as col
import sys
sys.setrecursionlimit(1000000)

def per_depth(nums):
    if len(nums) >= 5:
        perdep.append(nums)
        return
    for i in range(4):
        per_depth(nums + [i])


def permutation(nums):
    if len(nums) >= 5:
        if nums[::-1] not in perlist:
            perlist.append(nums)
        return
    for i in range(1, 6):
        if str(i) not in nums:
            permutation(nums + str(i))


def BFS(k, z):
    global answer
    if answer == 12:
        return
    num = perlist[k]
    turns = perdep[z]
    if not maze[num[4]][turns[4]][4][4]:
        return
    que = col.deque()
    visit = []
    if maze[num[0]][turns[0]][0][0]:
        que.append((0, 0, 0))
        visit.append((0, 0, 0))
    else:
        return
    cnt = 1
    while que:
        if cnt >= answer:
            return
        for _ in range(len(que)):
            depth, u, v = que.popleft()
            for i in range(6):
                if 0 <= depth + dirs[i][0] < 5 and 0 <= u + dirs[i][1] < 5 and 0 <= v + dirs[i][2] < 5:
                    if maze[num[depth + dirs[i][0]]][turns[depth + dirs[i][0]]][u + dirs[i][1]][v + dirs[i][2]]:
                        if (depth + dirs[i][0], u + dirs[i][1], v + dirs[i][2]) == (4, 4, 4):
                            answer = cnt
                            return
                        elif (depth + dirs[i][0], u + dirs[i][1], v + dirs[i][2]) not in visit:
                            que.append((depth + dirs[i][0], u + dirs[i][1], v + dirs[i][2]))
                            visit.append((depth + dirs[i][0], u + dirs[i][1], v + dirs[i][2]))
        cnt += 1


dirs = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]
perlist = []
perdep = []
maze = {'1': [], '2': [], '3': [], '4': [], '5': []}
answer = 60

for i in range(1, 6):
    maze[str(i)].append([list(map(int, input().split())) for _ in range(5)])

for num in range(1, 6):
    p1, p2, p3 = [[0]*5 for _ in range(5)], [[0]*5 for _ in range(5)], [[0]*5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            p1[i][j] = maze[str(num)][0][j][4-i]
            p2[i][j] = maze[str(num)][0][4-i][4-j]
            p3[i][j] = maze[str(num)][0][4-j][i]
        maze[str(num)].append(p1)
        maze[str(num)].append(p2)
        maze[str(num)].append(p3)
permutation('')
per_depth([])

for i in range(60):
    for j in range(len(perdep)):
        BFS(i, j)

if answer == 60:
    answer = -1
print(answer)
