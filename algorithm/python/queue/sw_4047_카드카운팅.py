from collections import deque
t = int(input())
for tc in range(1, t + 1):
    answer = []
    s = input()
    deck = deque([])
    string = ''
    dic = {'S':[], 'D':[], 'H':[], 'C':[]}
    for i in range(len(s) + 1):
        if i == len(s):
            deck.append(string)
        elif not i % 3:
            deck.append(string)
            string = s[i]
        else:
            string += s[i]
    deck.popleft()
    while deck:
        now = deck.popleft()
        if now[1:3] not in dic[now[0]] or int(now[1:3]) > 13 or int(now[1:3]) < 1:
            dic[now[0]] += [now[1:3]]
        else:
            answer = 'ERROR'
    if not answer:
        answer = [13 - len(dic['S']), 13 - len(dic['D']), 13 - len(dic['H']), 13 - len(dic['C'])]
    print('#{}'.format(tc), *answer) if type(answer) == type([]) else print('#{} '.format(tc), answer)