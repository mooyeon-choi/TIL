coin = [1, 4, 6]
choose = [0] * 100
def coinChange(k, n):
    if n == 0:
        for i in range(k):
            print(choose[i], end=' ')
        print()
        return
    for c in coin:
        if c > n: continue
        choose[k] = c
        coinChange(k + 1, n - c)

coinChange(0, 8)