for tc in range(1, int(input())+1):
    N, M, K = map(int, input().split())
    times = [0] + list(map(int, input().split())) + [11112]
    times.sort()
    answer = 'Possible'
    idx = 0
    for i in range(times[-2] + 1):
        for j in range(idx, len(times)):
            if times[j] > i or j == len(times) - 1:
                idx = j - 1
                break
        if i // M * K < idx:
            answer = 'Impossible'
            break
        elif idx == len(times) - 2:
            break

    print(f'#{tc} {answer}')