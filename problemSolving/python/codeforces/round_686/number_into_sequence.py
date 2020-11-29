def dfs(num, cnt, n_list):
    for i in range(2, int((num)**(1/2)) + 1):
        if not num % i:
            for n in n_list:
                if i % n:
                    break
            else:
                nums.append(i)
                cnt = dfs(num//i, cnt + 1, n_list + [i])
                if cnt > 1:
                    return cnt
                nums.pop()
    else:
        if cnt > 1:
            for n in n_list:
                if num % n:
                    return 1
            else:
                nums.append(num)
                return cnt
        else:
            return cnt

t = int(input())
for _ in range(t):
    num = int(input())
    nums = []
    result = dfs(num, 1, [1])
    print(result)
    if result > 1:
        print(' '.join(map(str, nums)))
    else:
        print(num)