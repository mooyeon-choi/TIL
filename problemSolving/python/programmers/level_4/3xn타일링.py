def solution(n):
    if n & 1:
        return 0
    else:
        memo = [1]
        for i in range(n//2):
            if not i:
                memo.append(3)
            elif i == 1:
                memo.append(memo[-1] * 3 + memo[-1] - memo[-2]) 
            else:
                memo.pop(0)
                memo.append(memo[-1] * 3 + memo[-1] - memo[-2])
        return memo[-1] % 1000000007