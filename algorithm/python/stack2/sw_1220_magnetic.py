for tc in range(1, 11):
    answer = 0
    n = int(input())
    m_field = [list(map(int, input().split())) for _ in range(100)]
    for i in range(100):
        for j in range(100):
            if m_field[j][i] == 1:
                now_number = 1
                if m_field[j][i] and m_field[j][i] != now_number and now_number == 1:
                    now_number = m_field[j][i]
                    answer += 1
                elif m_field[j][i] and m_field[j][i] != now_number:
                    now_number = m_field[j][i]
    print('#{} {}'.format(tc, answer))