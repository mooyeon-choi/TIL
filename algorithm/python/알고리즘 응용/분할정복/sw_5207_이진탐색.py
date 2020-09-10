t = int(input())
for tc in range(1, t + 1):
    answer = 0
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    B = list(map(int, input().split()))
    for num in B:
        lo = 0
        hi = n - 1
        dirs = 0
        while lo <= hi:
            mid = (lo + hi) >> 1
            if A[mid] == num:
                answer += 1
                break
            elif A[mid] < num and dirs != 1:
                lo = mid + 1
                dirs = 1
            elif A[mid] > num and dirs != -1:
                hi = mid - 1
                dirs = -1
            else:
                break
    print('#{} {}'.format(tc, answer))