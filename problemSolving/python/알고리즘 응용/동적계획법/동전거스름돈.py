coins = [6, 4, 1]
choose = []
memo = [-1] * 81
def coinChange(n): # n: 매개변수 , 문제의 크기(식별), 반환값: 문제의 해
    memo[0] = 0
    MIN = 0xffffff
    for coin in coins:
        if coin > n: continue
        ret = coinChange(n - coin) + 1
        if ret < MIN: MIN = ret
    memo[n] = MIN
    return MIN
print(coinChange(80))