def pre(v):
    if v == 0: return
    print(v, end=' ')
    pre(L[v])
    pre(R[v])

def inorder(v):
    if v == 0: return

    inorder(L[v])
    print(v, end=' ')
    inorder(R[v])

def post(v):
    if v == 0: return
    post(L[v])
    post(R[v])
    print(v, end=' ')

height = 0
def treeHeight(v, curH):
   if v == 0:
       global height
       height = max(height, curH - 1)
       return
   treeHeight(L[v], curH + 1)
   treeHeight(R[v], curH + 1)

def heightnode(v, count):
    if v == 0: return
    if count == 3:
        print(v, end=' ')
    heightnode(L[v], count + 1)
    heightnode(R[v], count + 1)

# 4. 트리의 노드 수. treeSize(v): v를 루트로 하는 트리의 노드 수 계산 ---
def treeSize(v):
   if v == 0: return
   global nodeCnt
   nodeCnt += 1
   treeSize(L[v])
   treeSize(R[v])

def route(u, v):
    if v == 0 or u == 0:
        print()
        return
    print(u, end=' ')
    route(P[u], v)

    print(v, end=' ')
    route(u, P[v])

V, E = map(int, input().split())
L = [0] * (V + 1)
R = [0] * (V + 1)
P = [0] * (V + 1)
arr = list(map(int, input().split()))

for i in range(0, E * 2, 2):
    u, v = arr[i], arr[i + 1]
    if L[u] == 0:
        L[u] = v
    else:
        R[u] = v
    P[v] = u

treeHeight(1, height)
print('# 2. 트리의 높이 : {}'.format(height))
pre(1)
print()
inorder(1)
print()
post(1)
print()
heightnode(1, 0)
print()
nodeCnt = 0
treeSize(3)
print(nodeCnt)
route(9, 13)