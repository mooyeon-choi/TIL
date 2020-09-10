def solution(n, k):
    answer = []
    numbers = list(range(1, n + 1))
    num = 1
    k -= 1
    for i in range(1, n):
        num *= i
    while k and len(numbers) > 1:
        answer.append(numbers.pop(k//num))
        k = k % num
        num //= len(numbers)
    answer += numbers
    return answer