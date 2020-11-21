t = int(input())
for tc in range(1, t + 1):
    answer = 0
    n, m = map(int, input().split())
    w_list = list(map(int, input().split()))
    t_list = list(map(int, input().split()))
    w_list = sorted(w_list, reverse=True)
    t_list = sorted(t_list, reverse=True)
    i = 0
    for t in t_list:
        for w in range(i, len(w_list)):
            if w_list[w] <= t:
                i = w + 1
                answer += w_list[w]
                break
    print('#{} {}'.format(tc, answer))