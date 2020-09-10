# 10번 반복
for tc in range(10):
    # 가로길이 입력
    n = int(input())
    # 빌딩 높이 입력
    b_list = list(map(int, input().split()))
    # 최종 결과값을 입력 받을 변수
    result = 0
    # 좌우 두칸을 제외한 범위에서 반복
    for i in range(2, n-2):
        # 주변건물에서 가장 높은 건물 (초기값 [i-2]위치의 건물 높이)
        max_value = b_list[i-2]
        # -2 ~ 2 사이에 있는 건물중 가장 높은 값을 찾는다
        for j in range(-1, 3):
            # 같은 건물은 제외하기위해 추가
            if j == 0: continue
            if b_list[i+j] > max_value:
                max_value = b_list[i+j]
        # 주변 건물중 가장 높은 건물보다 높을 경우에만 결과값에 추가
        if b_list[i] > max_value:
            result += b_list[i] - max_value
    print('#{} {}'.format(tc+1, result))