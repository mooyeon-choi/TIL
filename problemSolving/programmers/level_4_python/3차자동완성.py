def solution(words):
    words.sort()
    idx = 0
    end = len(words)
    result = [0]*end
    while idx < end - 1:
        for i in range(result[idx], len(words[idx])):
            for j in range(idx, end):
                if i >= len(words[j]):
                    break
                if words[j][i] != words[idx][i]:
                    break
                result[j] += 1
                if j < end - 1 and result[j] > result[j+1] + 1:
                    break
            if result[idx] > result[idx+1]:
                break
        idx += 1
    return sum(result) + 1