sol = {
    '112' : '0', '122' : '1', '221' : '2', '114' : '3', '231' : '4',
    '132' : '5', '411' : '6', '213' : '7', '312' : '8', '211' : '9'
}

for tc in range(1, int(input()) + 1):
    answer = 0
    n, m = map(int, input().split())
    words = [input() for _ in range(n)]
    bina = []
    results = []
    for word in words:
        if int(word, 16):
            if bin(int(word, 16))[2:] not in bina:
                bina.append(bin(int(word, 16))[2:])

    for bi in bina:
        idx = len(bi)
        code = ''
        i = len(bi) - 1
        while i >= 0:
            if bi[i] == '1':
                while len(code) < 8 and i >= 0:
                    if bi[i] == '1':
                        before = '1'
                        count = 0
                        code_num = []
                        code_number = ''
                        while len(code_num) < 3:
                            if i == -1:
                                code_num.append(count)
                                break
                            elif before != bi[i]:
                                before = bi[i]
                                code_num.append(count)
                                i -= 1
                                count = 1
                            else:
                                count += 1
                                i -= 1
                        min_num = 0xffff
                        for num in code_num:
                            if num < min_num:
                                min_num = num
                        for j in range(len(code_num)):
                            code_number += str(code_num[j] // min_num)
                        code += sol[code_number]
                        code_number = ''
                        code_num = []
                    else:
                        i -= 1
                if code not in results:
                    results.append(code)
                code = ''
            else:
                i -= 1
    for result in results:
        result = [int(num) for num in result]
        if not ((result[1] + result[3] + result[5] + result[7]) * 3 + result[6] + result[4] + result[2] + result[0]) % 10:
            answer += sum(result)
    print('#{} {}'.format(tc, answer))
