t = int(input())
for tc in range(1, t + 1):
    n, k = map(int, input().split())
    num_list = list(range(1, 13))
    result = 0
    for i in range(1 << 12):
        r_list = []
        for j in range(13):
            if i & (1 << j):
                r_list += [num_list[j]]
        if (len(r_list) == n) and (sum(r_list) == k):
            result += 1
    print('#{} {}'.format(tc, result))