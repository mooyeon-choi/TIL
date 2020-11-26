for tc in range(1, int(input()) + 1):
    answer = 0
    n, m = map(int, input().split())
    friend = [set() for _ in range(n+1)]
    for _ in range(m):
        i, j = map(int, input().split())
        if i == 1:
            friend[j] = i
        elif j == 1:
            friend[i] = j
        else:
            try:
                friend[i].add(j)
            except:
                pass
            try:
                friend[j].add(i)
            except:
                pass
    for i in range(2, n+1):
        if friend[i] == 1:
            answer += 1
        else:
            for fri in friend[i]:
                if friend[fri] == 1:
                    answer += 1
                    break

    print('#{} {}'.format(tc, answer))