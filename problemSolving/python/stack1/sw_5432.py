t = int(input())
for tc in range(1, t + 1):
    bracket = list(input())
    stick = []
    stick.append(bracket.pop())
    r = 0
    answer = 0
    for i in range(len(bracket) -1, -1, -1):
        if bracket[i] == '(' and r == 0:
            bracket.pop()
            stick.pop()
            answer += len(p)
            r = 1
        elif bracket[i] == '(':
            bracket.pop()
            stick.pop()
            answer += 1
        else:
            stick.append(bracket.pop())
            r = 0
    print('#{} {}'.format(tc, answer))