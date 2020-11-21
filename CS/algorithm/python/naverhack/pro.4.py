def Solution(A, B):
    answer = 0
    num = A * B
    while num != 0:
        answer += num%2
        num //= 2
    return answer