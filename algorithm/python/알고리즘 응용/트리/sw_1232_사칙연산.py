def cal(w):
    if V[w] == '*':
        return cal(L[w]) * cal(R[w])
    elif V[w] == '+':
        return cal(L[w]) + cal(R[w])
    elif V[w] == '/':
        return cal(L[w]) / cal(R[w])
    elif V[w] == '-':
        return cal(L[w]) - cal(R[w])
    else:
        return V[w]



for tc in range(1, 11):
    result = []
    N = int(input())
    L = [0]*(1+N)
    R = [0]*(1+N)
    V = [0]*(1+N)
    for _ in range(N):
        value = list(input().split())
        for i in range(1, len(value)):
            if not V[int(value[0])]:
                try:
                    V[int(value[0])] = int(value[i])
                except:
                    V[int(value[0])] = value[i]
            elif not L[int(value[0])]:
                L[int(value[0])] = int(value[i])
            else:
                R[int(value[0])] = int(value[i])

    print('#{} {}'.format(tc, int(cal(1))))