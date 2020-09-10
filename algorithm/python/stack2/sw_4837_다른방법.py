def subset(num, n):       # k = 현재 노드의 높이, n = 단말 노드의 높이
    global sum_, answer
    if num == 12:          # 모든선택이 완료, 단말노드에 도착
        sum_ = 0
        for i in range(k):
            if bits[i]:
                sum_ += arr[i]
        if sum(bits) == n:
            if sum_ == k:
                answer += 1
                print(bits)
            return
    # 선택이 남아있다.
    bits[num] = 1; subset(num + 1, n)    # 왼쪽
    bits[num] = 0; subset(num + 1, n)    # 오른쪽


t = int(input())
for tc in range(1, t + 1):
    answer = 0
    n, k = map(int, input().split())
    bits = [0] * k
    arr = [number for number in range(1, k+1)]
    sum_ = 0
    subset(0, n)
    print('#{} {}'.format(tc, answer))