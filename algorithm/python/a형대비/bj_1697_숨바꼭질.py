from collections import deque


def bfs():
    value = deque()
    value.append(n)
    count = 0
    while True:
        for _ in range(len(value)):
            num = value.popleft()
            visit[num] = 1
            if num == k:
                return count
            if num + 1 <= k and not visit[num + 1]:
                value.append(num + 1)
            if num - 1 >= 0 and not visit[num - 1]:
                value.append(num - 1)
            if num * 2 <= 100000 and not visit[num * 2]:
                value.append(num * 2)
        count += 1


n, k = map(int, input().split())
visit = [0]*100001
if k < n:
    min_num = n - k
else:
    min_num = bfs()
print(min_num)