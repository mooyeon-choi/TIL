t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    a_i = list(map(int, input().split()))
    result = []
    for i in range(n//2):
        max_num = a_i[0]
        min_num = a_i[0]
        max_idx = min_idx = 0
        for idx in range(len(a_i)):
            if a_i[idx] > max_num:
                max_num = a_i[idx]
                max_idx = idx
            if a_i[idx] < min_num:
                min_num = a_i[idx]
                min_idx = idx
        result.append(str(a_i.pop(max_idx)))
        if min_idx > max_idx:
            result.append(str(a_i.pop(min_idx - 1)))
        else:
            result.append(str(a_i.pop(min_idx)))
        if len(result) == 10:
            break
    print('#{} '.format(tc) + ' '.join(result))