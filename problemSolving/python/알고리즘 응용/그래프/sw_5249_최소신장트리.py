for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    nums = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        nums[u].append((v, w))
        nums[v].append((u, w))

    pi = [0] * (n + 1)
    maxnum = [0] + [0xffffff] * n
    visit = [0] * (n + 1)
    cnt = n + 1
    while cnt:
        x, MIN = 0, 0xffffff
        for i in range(n+1):
            if not visit[i] and maxnum[i] < MIN: x, MIN = i, maxnum[i]
        visit[x] = True

        for v, w in nums[x]:
            if not visit[v] and w < maxnum[v]:
                maxnum[v] = w
                pi[v] = x
        cnt -= 1
    print('#{} {}'.format(tc, sum(maxnum)))
