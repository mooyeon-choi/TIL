for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    friend = list(map(int, input().split()))
    human = [[] for _ in range(n+1)]
    for i in range(0, len(friend), 2):
        human[friend[i]].append(friend[i+1])
        human[friend[i+1]].append(friend[i])
    cnt = [0]*(n+1)
    for i in range(1, n+1):
        for num in human[i]:
            if cnt[num]:
                if cnt[i]:
                    cnt[i] = cnt[num]
        else:
            cnt[i] = i
    print(cnt)
    print('#{} {}'.format(tc, len(set(cnt))-1))