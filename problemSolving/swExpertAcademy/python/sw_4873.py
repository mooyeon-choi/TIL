t = int(input())

for tc in range(1, t + 1):
    words = list(input())
    count = 1
    result = []
    while count:
        count = 0
        for i in range(len(words)):
            if not result:
                result.append(words[i])
            elif result[-1] == words[i]:
                result.pop()
                count += 1
            else:
                result.append(words[i])
        words, result = result, []
    print('#{} {}'.format(tc, len(words)))
