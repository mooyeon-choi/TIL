sol = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']

t = int(input())
for tc in range(1, t + 1):
    answer = 0
    n, m = map(int, input().split())
    code = [input() for _ in range(n)]
    idx = 0
    line = 0
    result = []
    for i in range(n):
        for j in range(m-1, -1, -1):
            if code[i][j] == '1':
                line = i
                idx = j - 55
                break

    for i in range(8):
        num = ''
        for j in range(7):
            num += code[line][idx + i * 7 + j]
        for j in range(10):
            if num == sol[j]:
                result.append(j)
    if not ((result[0] + result[2] + result[4] + result[6])*3 + result[1] + result[3] + result[5] + result[7]) % 10:
        answer = sum(result)
    print('#{} {}'.format(tc, answer))