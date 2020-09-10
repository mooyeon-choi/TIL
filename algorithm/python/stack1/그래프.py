import sys; sys.stdin = open('DFS_input.txt', 'r')

def DFS(v):
    # 시작점을 방문하고, 스택에 push
    S = []
    visit[v] = True; print(v, end=' ')
    S.append(v)
    # 빈스택이 아닐동안 반복
    while S:
        for w in G[v]:
            # v의 방문하지 않은 인접정점 w에 찾아서
            if not visit[w]:
                # w를 방문하고, v를 스택에 push
                visit[w] = True; print(w, end=' ')
                S.append(v)
                # v를 w로 설정
                v = w
                break
        # 인접정점이 없다면, 스택에서 pop()해서
        else:
            # v로 설정
            v = S.pop()

V, E = map(int, input().split()) # 정점수, 간선수
G = [[] for _ in range(V + 1)]   # 1 ~ v 까지
visit = [False] * (V + 1)

for _ in range(E):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

for i in range(1, V + 1):
    print(i, '-->', G[i])