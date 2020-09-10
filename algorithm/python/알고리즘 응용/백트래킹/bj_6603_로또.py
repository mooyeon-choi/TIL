while True:
    num_list = list(map(int, input().split()))
    if len(num_list) == 1:
        break
    numlist = num_list[1:]
    n = len(numlist)
    for a in range(n):
        for b in range(a + 1, n):
            for c in range(b + 1, n):
                for d in range(c+1,n):
                    for e in range(d+1,n):
                        for f in range(e+1,n):
                            print(numlist[a], numlist[b], numlist[c], numlist[d], numlist[e], numlist[f])
    print('')