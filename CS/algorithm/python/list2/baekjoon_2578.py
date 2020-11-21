def bingo(list1, list2):
    count = 0
    result_list = []
    for _ in range(5):
        result_list.append([0, 0, 0, 0, 0])
    for say in list2:
        count += 1
        bingo_count = 0
        x_list = [[], [], [], [], []]
        y_list = [[], [], [], [], []]
        d_list = [[], []]
        for j in range(5):
            for k in range(5):
                if list1[j][k] == say:
                    result_list[j][k] = 1
        for j in range(5):
            for k in range(5):
                x_list[j].append(result_list[j][k])
                y_list[j].append(result_list[k][j])
                if j == 0:
                    d_list[j].append(result_list[k][k])
                elif j == 1:
                    d_list[j].append(result_list[4-k][k])
        for j in range(5):
            n_sum = 0
            for k in x_list[j]:
                n_sum += k
            if n_sum == 5:
                bingo_count += 1
            n_sum = 0
            for k in y_list[j]:
                n_sum += k
            if n_sum == 5:
                bingo_count += 1
            n_sum = 0
            if j < 2:
                for k in d_list[j]:
                    n_sum += k
                if n_sum == 5:
                    bingo_count += 1
        if bingo_count >= 3:
            return count


b_list = []
say_list = []
for b in range(5):
    b_list.append(list(map(int, input().split())))
for i in range(5):
    say_list += list(map(int, input().split()))


print(bingo(b_list, say_list))