for tc in range(1, 11):
    tc_num = input()
    result_list = []
    y_list = []
    for i in range(100):
        y_list.append(list(map(int, input().split())))
    for i in range(100):
        x_sum = 0
        y_sum = 0
        d_sum = 0
        for j in range(100):
            x_sum += y_list[i][j]
            y_sum += y_list[j][i]
            if i == 0:
                d_sum += y_list[j][j]
            elif i == 99:
                d_sum += y_list[99-j][99-j]
        result_list.append(x_sum)
        result_list.append(y_sum)
        if i == 0 or i == 99:
            result_list.append(d_sum)
    result = result_list[0]
    for number in result_list:
        if number > result:
            result = number
    print('#{} {}'.format(tc, result))