t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    result = ''
    for word in range(n):
        string, number = map(str, input().split())
        for i in range(int(number)):
            if len(result) % 11:
                result += string
            else:
                result += '\n' + string
    print(f'#{tc} {result}')