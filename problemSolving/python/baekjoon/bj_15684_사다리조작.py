def back(i, j, c): # i현재 행, j현재열, c추가선 개수
   if c > 3:
       return
   if i == H: # 마지막 행
       for x in range(1, len(pos)):
           if pos[x] != x:  return
       global MIN
       if MIN != -1:
           MIN = min(MIN, c)
       else:
           MIN = c
       return
   if j < N and visit[i + 1][j]: # 오른쪽
       pos[j], pos[j + 1] = pos[j + 1], pos[j]
       if j >= N - 2: back(i + 1, 1, c)
       else: back(i, j + 2, c)
       return
   else:
       if j < N:
           # 사다리 놓기
           if not visit[i + 1][j] and (j >= N - 1 or not visit[i + 1][j + 1]) \
                   and (j - 1 < 1 or not visit[i + 1][j - 1]):
               pos[j], pos[j + 1] = pos[j + 1], pos[j]
               if j >= N - 2: back(i + 1, 1, c + 1)
               else: back(i, j + 2, c + 1)
               pos[j], pos[j + 1] = pos[j + 1], pos[j]
           # 그냥 가기
           if j >= N - 1: back(i + 1, 1, c)
           else: back(i, j + 1, c)
       back(i + 1, j, c) # 그냥 내려가기
N, M, H = map(int, input().split()) # N: 세로선 개수, M: 존재하는 가로선 개수, H: 가로선 개수
visit = [[False] * N for _ in range(H + 1)] # 1~N-1, 세로선/ 1~M 가로선
for _ in range(M):
   a, b = map(int, input().split())
   visit[a][b] = True
MIN = -1
pos = [0] + [x for x in range(1, N + 1)]
back(0, 1, 0)
print(MIN)