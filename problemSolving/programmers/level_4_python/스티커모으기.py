def solution(sticker):
    if len(sticker) < 4:
        return max(sticker)
    memo = [0] * len(sticker)
    for i in range(len(sticker)):
        if not i:
            continue
        elif i == 1:
            memo[i] = sticker[i]
        elif i == 2:
            memo[i] = sticker[i]
            sticker[i] += sticker[0]
        elif i == len(sticker) - 1:
            memo[i] = sticker[i] + max(memo[i-2], memo[i-3])
        else:
            memo[i] = sticker[i] + max(memo[i-2], memo[i-3])
            sticker[i] += max(sticker[i-2], sticker[i-3])
    
    return max(memo[-1], memo[-2], sticker[-2], sticker[-3])