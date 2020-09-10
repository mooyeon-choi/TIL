t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    room = []
    room_sort = []
    result = []
    used = []
    count = 0
    for _ in range(n):
        r_1, r_2 = map(int, input().split())
        if r_1 < r_2:
            r = [r_1, r_2]
        else:
            r = [r_2, r_1]
        room.append(r)
    for i in range(n):
        min_idx = 0
        min_num = 401
        for j in range(len(room)):
            if room[j][0] < min_num:
                min_num = room[j][0]
                min_idx = j
        ap_list = room.pop(min_idx)
        room_sort.append(ap_list)
    for i in range(n):
        if i not in used:
            result.append(room_sort[i])
            used.append(i)
            for j in range(i, n):
                if j not in used:
                    if (result[count][-1] + 1) // 2 < (room_sort[j][0] + 1) // 2:
                        result[count] += room_sort[j]
                        used.append(j)
            count += 1
    print('#{} {}'.format(tc, len(result)))
