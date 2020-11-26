t = int(input())
for tc in range(1, t + 1):
    fee = list(map(int, input().split()))
    use = list(map(int, input().split()))
    memo = [[0]*12 for _ in range(4)]
    for i in range(4):
        for j in range(12):
            if not i:
                memo[i][j] = use[j]*fee[i]
            if i == 1:
                if memo[i-1][j] > fee[i]:
                    memo[i][j] = fee[i]
                else:
                    memo[i][j] = memo[i-1][j]
    for i in range(4):
        print(memo[i])