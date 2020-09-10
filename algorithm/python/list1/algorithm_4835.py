t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().split())
    a_i = list(map(int, input().split()))
    result_list = []
    if m % 2:
        for i in range(m//2, n - m//2):
            num_sum = 0
            for j in range(-(m//2), m//2 + 1):
                num_sum += a_i[i+j]
            result_list.append(num_sum)
    else:
        for i in range(m//2, n - (m//2) + 1):
            num_sum = 0
            for j in range(-(m//2), m//2):
                num_sum += a_i[i+j]
            result_list.append(num_sum)
    max_num = result_list[0]
    min_num = result_list[0]
    for number in result_list:
        if number > max_num:
            max_num = number
        if number < min_num:
            min_num = number
    result = max_num - min_num
    print('#{} {}'.format(tc, result))