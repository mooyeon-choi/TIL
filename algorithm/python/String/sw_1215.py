for tc in range(1, 11):
    n = int(input())
    str_list = []
    word_list = []
    result = 0
    for _ in range(8):
        str_list.append(input())
    for i in range(8):
        for j in range(8 - n + 1):
            string_1, string_2 = '', ''
            for k in range(n):
                string_1 += str_list[i][j+k]
                string_2 += str_list[j+k][i]
            word_list.append(string_1)
            word_list.append(string_2)
    for word in word_list:
        for num in range(n//2):
            if word[num] != word[-1 - num]:
                break
        else:
            result += 1
    print('#{} {}'.format(tc, result))