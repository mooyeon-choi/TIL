def solution(food_times, k):
    answer = 0
    left = 0
    right = max(food_times)
    while left < right - 1:
        numsum = 0
        center = (left + right) // 2
        for time in food_times:
            if time < center:
                numsum += time
            else:
                numsum += center
        if numsum == k:
            left = center
            break
        elif numsum < k:
            left = center
        else:
            right = center
    for i in range(len(food_times)):
        if food_times[i] > left:
            food_times[i] -= left
            k -= left
        else:
            k -= food_times[i]
            food_times[i] = 0
    for i in range(len(food_times)):
        if food_times[i]:
            if k == 0:
                answer = i + 1
                break
            else:
                k -= 1
    else:
        answer = -1
    return answer