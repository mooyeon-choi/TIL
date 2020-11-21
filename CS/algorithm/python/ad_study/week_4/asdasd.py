def solution(msg):
    answer = []
    dictionary = dict()
    for num in range(ord('A'), ord('Z')+1):
        dictionary[chr(num)] = num + 1 - ord('A')
    start = 0
    end = len(msg)
    length = 26
    while start <= end-1:
        tmp = ''
        for ch in range(start, end):
            if dictionary.get(tmp + msg[ch]):
                tmp += msg[ch]
            else:
                start = ch + 1
                length += 1
                answer.append(dictionary[tmp])
                dictionary[tmp + msg[ch]] = length
                break
    print(answer)
    return answer

solution("TOBEORNOTTOBEORTOBEORNOT")