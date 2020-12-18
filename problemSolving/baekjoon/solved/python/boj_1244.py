n = int(input())
switch = list(map(int, input().split()))
t = int(input())
for tc in range(t):
    p, num = map(int, input().split())
    if p == 1:
        for i in range(n):
            if not (i + 1) % num:
                switch[i] = int(not switch[i])
    elif p == 2:
        switch[num - 1] = int(not switch[num - 1])
        for i in range(1, n):
            if num - 1 - i > -1 and num - 1 + i < n:
                if switch[num - 1 - i] == switch[num - 1 + i]:
                    switch[num - 1 - i], switch[num - 1 + i] = int(not switch[num - 1 - i]), int(not switch[num - 1 + i])
                else:
                    break
result = ''
for number in range(0, len(switch)):
    if number == 0:
        result += str(switch[number])
    elif not number % 20:
        result += '\n' + str(switch[number])
    else:
        result += ' ' + str(switch[number])
print(result)