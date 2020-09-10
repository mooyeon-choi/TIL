from collections import deque

def dfs():
    count = 0
    used = ''
    a = deque()
    a.append((0, 0))
    while a:
        for _ in range(len(a)):
            i, j = a.popleft()
            used += alph[i][j]
            print(used)
            for k in range(4):
                if 0 <= i+x[k] < r and 0 <= j+y[k] < c:
                    if alph[i+x[k]][j+y[k]] not in used:
                        used += alph[i+x[k]][j+y[k]]
                        a.append((i+x[k], j+y[k]))
        count += 1
    return count


x = [-1, 1, 0, 0]
y = [0, 0, -1, 1]
r, c = map(int, input().split())
alph =[list(input()) for _ in range(r)]
print(dfs())