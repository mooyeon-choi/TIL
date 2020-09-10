t = int(input())
for tc in range(1, t + 1):
    answer = 0
    bi = input()
    tr = input()
    bi_list = []
    for i in range(len(bi)):
        num = list(bi)
        if bi[i] == '0':
            num[i] = '1'
        else:
            num[i] = '0'
        bi_list.append(int(''.join(num), 2))

    for i in range(len(tr)):
        for j in range(3):
            num = list(tr)
            if str(j) != tr[i]:
                num[i] = str(j)
                num = ''.join(num)
                if int(num, 3) in bi_list:
                    answer = int(num, 3)

    print('#{} {}'.format(tc, answer))