def back(i, num, count):
    global answer
    if count >= answer:
        return
    if num + i >= len(station):
        answer = count
        return
    for j in range(num + i, i, - 1):
        back(j, station[j], count + 1)


t = int(input())
for tc in range(1, t + 1):
    station = list(map(int, input().split()))
    answer = len(station) - 1
    back(1, station[1], 0)
    print('#{} {}'.format(tc, answer))