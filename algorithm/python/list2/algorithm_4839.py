t = int(input())
for tc in range(1, t + 1):
    p, a, b = map(int, input().split())
    count_a = count_b = 0
    page_r = p
    page_l = 1
    page = int((page_l + page_r ) / 2)
    while page_r >= page_l:
        count_a += 1
        if page > a:
            page_r = page
        elif page < a:
            page_l = page
        if page == a:
            break
        page = int((page_l + page_r) / 2)
    page_r = p
    page_l = 1
    page = page_r // 2
    while page_r >= page_l:
        count_b += 1
        if page > b:
            page_r = page
        elif page < b:
            page_l = page
        if page == b:
            break
        page = int((page_l + page_r) / 2)
    if count_a > count_b:
        result = 'B'
    elif count_a < count_b:
        result = 'A'
    else:
        result = 0
    print('#{} {}'.format(tc, result))