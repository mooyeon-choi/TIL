t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    # 숫자 string으로 받아오기
    a_i = input()
    result = [0]*10
    for i in a_i:
        for j in range(10):
            if j == int(i):
                result[j] += 1
    max_amo = 0
    max_num = 0
    for number in range(10):
        if max_amo <= result[number]:
            max_num = number
            max_amo = result[number]
    print('#{} {} {}'.format(tc, max_num, max_amo))