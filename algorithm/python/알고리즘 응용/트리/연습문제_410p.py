V, E = map(int, input().split())
L = [0] * (V + 1)
R = [0] * (V + 1)
P = [0] * (V + 1)

arr = list(map(int, input().split()))
for i in range(0, E * 2, 2):
    p, c = arr[i], arr[i + 1]
    if L[p] == 0: L[p] = c
    else: R[p] = c
    P[c] = p

def inorder(v):
    inorder(L[v])
    inorder(R[v])
inorder(1)