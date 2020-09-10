t = int(input())
for tc in range(1, t + 1):
    word = input()
    result = 'Exist'
    for i in range(len(word)//2):
        if word[i] == word[-1 - i] or word[i] == '?' or word[-1 - i] == '?':
            continue
        else:
            result = 'Not exist'
            break
    print('#{} {}'.format(tc, result))