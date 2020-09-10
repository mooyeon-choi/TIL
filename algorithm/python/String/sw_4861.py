t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().split())
    word_list = []
    result = ''
    for i in range(n):
        word_list.append(input())
    string_list = []
    for i in range(n):
        for j in range(n - m + 1):
            string_1, string_2 ='', ''
            for k in range(m):
                string_1 += word_list[i][j+k]
                string_2 += word_list[j+k][i]
            string_list.append(string_1)
            string_list.append(string_2)
    for word in string_list:
        for num in range(m//2):
            if word[num] != word[-1-num]:
                break
        else:
            result = word
            break
    print('#{} {}'.format(tc, result))