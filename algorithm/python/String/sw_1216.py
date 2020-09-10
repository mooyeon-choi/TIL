for _ in range(10):
    tc = int(input())
    str_list = []
    result = []
    for _ in range(100):
        str_list.append(input())
    for n in range(1, 100):
        for i in range(100):
            for j in range(100 - n):
                word_1 = ''
                word_1 += str_list[i][j:j+n]
                if text == text[::-1]:
                    result.append(len(text))
                    break

    print('#{} {}'.format(tc, max_num))