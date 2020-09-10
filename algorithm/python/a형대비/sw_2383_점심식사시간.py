for tc in range(1, int(input()) + 1):
    n = int(input())
    room = [list(map(int, input().split())) for _ in range(n)]
    persons = []
    stairs = []
    stair_lenth = [0]*2
    answer = 0xffffff
    for i in range(n):
        for j in range(n):
            if room[i][j] == 1:
                persons.append((i, j))
            elif room[i][j]:
                stairs.append((i, j))
                if not stair_lenth[0]:
                    stair_lenth[0] = room[i][j]
                else:
                    stair_lenth[1] = room[i][j]
    lenth = [[] for _ in range(len(stairs))]
    for i in range(len(stairs)):
        for person in persons:
            lenth[i].append(abs(stairs[i][0] - person[0]) + abs(stairs[i][1] - person[1]))
    for i in range(1 << len(persons)):
        first = [0] * len(persons)
        for j in range(len(persons)):
            if i & 1 << j:
                first[j] = 1
        firstWait = []
        nextWait = []
        for j in range(len(persons)):
            if first[j]:
                firstWait.append(lenth[0][j])
            else:
                nextWait.append(lenth[1][j])
        firstWait.sort()
        nextWait.sort()
        time1 = 0
        for k in range(len(firstWait)):
            if k < 3:
                pass
            elif firstWait[k] - firstWait[k - 3] < stair_lenth[0]:
                time1 = firstWait[k - 3] + 2 * stair_lenth[0]
            else:
                time1 = firstWait[k] + stair_lenth[0]
        if firstWait and len(firstWait) <= 3:
            time1 = firstWait[-1] + stair_lenth[0]
        time2 = 0
        for k in range(len(nextWait)):
            if k < 3:
                pass
            elif nextWait[k] - nextWait[k - 3] < stair_lenth[1]:
                time2 = nextWait[k - 3] + 2 * stair_lenth[1]
            else:
                time2 = nextWait[k] + stair_lenth[1]
        if nextWait and len(nextWait) <= 3:
            time2 = nextWait[-1] + stair_lenth[1]
        if answer > max(time1, time2):
            answer = max(time1, time2)
    print('#{} {}'.format(tc, answer + 1))
