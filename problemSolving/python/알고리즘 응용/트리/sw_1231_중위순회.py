def inorder(v):
    if v == 0: return

    inorder(L[v])
    print(word[v], end='')
    inorder(R[v])

for tc in range(1, 11):
    print('#{} '.format(tc), end='')
    n = int(input())
    L = [0] * (n + 1)
    R = [0] * (n + 1)
    P = [0] * (n + 1)
    word = [0]*(n+1)
    for _ in range(n):
        node = list(input().split())
        word[int(node[0])] = node[1]
        for i in range(2, len(node)):
            if L[int(node[0])] == 0:
                L[int(node[0])] = int(node[i])
            else:
                R[int(node[0])] = int(node[i])
            P[int(node[i])] = int(node[0])
    inorder(1)
    print()
