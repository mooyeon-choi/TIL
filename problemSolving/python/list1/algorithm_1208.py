# tc 1~191001 까지 반복
for tc in range(1, 11):
    # 입력값 받아오기
    n = int(input())
    b_list = list(map(int, input().split()))
    for i in range(n):
        # 리스트에서 최대값, 최소값 idx를 저장할 변수
        max_idx, min_idx = 0, 0
        max_num = b_list[0]
        min_num = b_list[0]
        # b_list에서 최대값, 최소값 찾기
        for j in range(100):
            if max_num < b_list[j]:
                max_num = b_list[j]
                max_idx = j
            if min_num > b_list[j]:
                min_num = b_list[j]
                min_idx = j
        # 최대값은 -1, 최소값은 +1
        b_list[max_idx] -= 1
        b_list[min_idx] += 1
    # 최대값, 최소값 다시 초기화
    max_num = b_list[0]
    min_num = b_list[0]

    # N번 실행 후 최대값, 최소값 찾기
    for num in b_list:
        if max_num < num:
            max_num = num
        if min_num > num:
            min_num = num
    print('#{} {}'.format(tc, max_num - min_num))