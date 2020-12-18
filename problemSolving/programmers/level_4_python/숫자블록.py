def solution(begin, end):
    answer = []
    for num in range(begin, end+1):
        if num == 1:
            answer.append(0)
        else:
            for i in range(2, int(num**0.5) + 1):
                if not num % i and num / i <= 10000000:
                    answer.append(num/i)
                    break
            else:
                answer.append(1)
    return answer