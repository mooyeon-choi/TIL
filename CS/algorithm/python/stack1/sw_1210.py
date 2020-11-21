for _ in range(10):
    tc = int(input())
    map_list = []
    num = 0
    num_i, num_j = 0, 0
    for _ in range(100):
        map_list.append(list(map(int, input().split())))
    for i in range(len(map_list[99])):
        if map_list[99][i] == 2:
            num = i
    for i in range(98, -1, -1):
        for j in range(-1, 2):
            if j != 0 and -1 < num + j < 100:
                if map_list[i][num + j]:
                    if j < 0:
                        while (map_list[i][num - 1]):
                            num -= 1
                            if num == 0:
                                break
                    if j > 0:
                        while (map_list[i][num + 1]):
                            num += 1
                            if num == 99:
                                break
                    break
    print('#{} {}'.format(tc, num))