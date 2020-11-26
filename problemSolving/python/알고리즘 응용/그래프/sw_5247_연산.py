from collections import deque

for tc in range(1, int(input()) + 1):
    answer = 0
    n, m = map(int, input().split())
    que = deque([n])
    used = [0]*(10**6 + 1)
    while que:
        for _ in range(len(que)):
            num = que.popleft()
            if num == m:
                break
            if num + 1 <= 10**6 and not used[num + 1]:
                que.append(num + 1)
                used[num + 1] = 1
            if num - 1 >= 0 and not used[num - 1]:
                que.append(num - 1)
                used[num - 1] = 1
            if num * 2 <= 10**6 and not used[num * 2]:
                que.append(num * 2)
                used[num * 2] = 1
            if num - 10 >= 0 and not used[num - 10]:
                que.append(num - 10)
                used[num - 10] = 1
        if num == m:
            break
        answer += 1
    print('#{} {}'.format(tc, answer))