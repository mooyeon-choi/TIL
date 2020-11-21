n = int(input())
dp = [0] + [int(input()) for _ in range(n)]
for i in range(n, -1, -1):
    if i == n:
        continue
    elif i == n - 1:
        dp[i] = [0, dp[i] + dp[n]]
    elif i == n - 2:
        dp[i] = [dp[i] + dp[n], dp[i] + dp[n]]
    elif i == 0:
        dp[i] = dp[i+2] + dp[i+1]
    else:
        dp[i] = [dp[i] + max(dp[i+2]), dp[i] + dp[i+1][0]]
print(max(dp[0]))