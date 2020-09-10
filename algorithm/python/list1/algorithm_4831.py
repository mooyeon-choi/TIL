t = int(input())
for tc in range(1, t + 1):
    k, n, m = map(int, input().split())
    m_list = list(map(int, input().split()))
    n_list = [0]*n + [1]
    # 현재 충전소 위치, 충전할 위치, 이전 충전소 위치
    nch, ch, pch = 0, 0, 0
    # 충전횟수를 저장할 결과값 변수
    result = 0
    # 충전소 위치와 같은 n_list의 idx값에 1을 넣어줌
    for i in m_list:
        n_list[i] = 1
    for i in range(n+1):
        if n_list[i] == 1:
            nch = i
            if nch - ch > k:
                if pch - ch <= k:
                    ch = pch
                    result += 1
                else:
                    result = 0
                    break
            pch = i
    print('#{} {}'.format(tc, result))