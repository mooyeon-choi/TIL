def order(v):
    global count
    if not v: return
    order(L[v])
    result[v] = count
    count += 1
    order(R[v])

t = int(input())
for tc in range(1, t + 1):
    count = 1
    n = int(input())
    for i in range(100):
        if n < 2**i:
            E = i
            break
    L = [0]*(n+1)
    R = [0]*(n+1)
    result = [0]*(n+1)
    for i in range(1, E + 1):
        if i * 2 < n + 1:
            L[i] = i * 2
        if i * 2 + 1 < n + 1:
            R[i] = i * 2 + 1
    order(1)
    print('#{} {} {}'.format(tc, result[1], result[n//2]))