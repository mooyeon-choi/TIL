for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    test_case = list(map(int, input().split()))
    printed = [0]*N
    idx, cnt = 0, 0
    while not printed[M]:
        maxidx = 0
        maxnum = 0
        for i in range(N):
            if not printed[(idx + i)%N] and maxnum < test_case[(idx + i)%N]:
                maxidx = idx + i
                maxnum = test_case[(idx + i)%N]
        printed[maxidx % N] = 1
        idx = maxidx
        cnt += 1
    print(cnt)