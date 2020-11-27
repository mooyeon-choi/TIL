def dfs(num, cnt, n):
    for i in range(max(n, 2), num // 2, n):
        if not num % i:
            if not i % n:
                nums.append(i)
                return dfs(num//i, cnt + 1, n * i)
    else:
        nums.append(num)
        return cnt

t = int(input())
for _ in range(t):
    num = int(input())
    nums = []
    print(dfs(num, 1, 1))
    print(' '.join(map(str, nums)))