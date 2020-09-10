def dfs(numbers, cnt):
    global answer
    if cnt == int(count):
        if int(''.join(numbers)) > int(answer):
            answer = ''.join(numbers)
        return
    if ''.join(numbers) + str(cnt) in numset:
        return
    else:
        numset.add(''.join(numbers) + str(cnt))
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            numbers[i], numbers[j] = numbers[j], numbers[i]
            dfs(numbers, cnt + 1)
            numbers[i], numbers[j] = numbers[j], numbers[i]

t = int(input())
for tc in range(1, t + 1):
    answer, count = input().split()
    number = list(answer)
    numset = set()
    dfs(number, 0)
    print('#{} {}'.format(tc, ''.join(answer)))