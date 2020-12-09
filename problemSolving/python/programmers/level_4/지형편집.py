def solution(land, P, Q):
    nums = {}
    for i in range(len(land)):
        for j in range(len(land)):
            if land[i][j] not in nums:
                nums[land[i][j]] = 1
            else:
                nums[land[i][j]] += 1

    pivots = sorted(nums.keys())
    p = nums[pivots[0]]
    q = sum(nums.values()) - nums[pivots[0]]
    before = pivots[0]
    result = 0
    for key, value in sorted(nums.items()):
        result += (key - pivots[0]) * Q * value
    answer = result
    for i in range(1, len(pivots)):
        result -= (pivots[i] - before) * Q * q
        result += (pivots[i] - before) * P * p
        before = pivots[i]
        p += nums[pivots[i]]
        q -= nums[pivots[i]]
        if result < answer:
            answer = result
        
    return answer