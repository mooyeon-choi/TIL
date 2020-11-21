# 테스트 케이스 갯수 입력
t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    a_i = list(map(int, input().split()))
    min_num = 1000000 # 예외케이스 발생가능
    max_num = 0       # 초기값에 a_i 첫번째 값 넣어주는 것은 어떨까
    # n까지 반복
    for i in range(n):
        # max_num 보다 클경우 max_num으로 설정
        if a_i[i] > max_num:
            max_num = a_i[i]
        # min_num 보다 작을 경우 min_num으로 설정
        if a_i[i] < min_num:
            min_num = a_i[i]
    result = max_num - min_num
    print('#{} {}'.format(tc, result))