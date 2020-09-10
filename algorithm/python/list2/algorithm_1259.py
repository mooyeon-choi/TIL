t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    n_list = list(map(int, input().split()))
    nasa_list = []
    result_list = []
    result_str = ''
    for i in range(n):
        nasa_list.append([n_list[i*2], n_list[i*2+1]])
    result_list = nasa_list[0]
    for i in range(n-1):
        for nasa in nasa_list:
            if result_list[0] == nasa[1]:
                result_list = nasa + result_list
            elif result_list[-1] == nasa[0]:
                result_list = result_list + nasa
    for num in range(2 * n):
        if num != 2 * n - 1:
            result_str += str(result_list[num]) + ' '
        else:
            result_str += str(result_list[num])
    print('#{} {}'.format(tc, result_str))