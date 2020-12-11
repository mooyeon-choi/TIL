def solution(distance, rocks, n):
    right = distance
    left = 0
    while left < right:
        dist = [0] + sorted(rocks) + [distance]
        cnt = 0
        mid = (right + left + 1) // 2
        ridx, lidx = 1, 0
        while ridx < len(dist):
            if dist[ridx] - dist[lidx] < mid:
                if ridx == len(dist) - 1:
                    before = dist[lidx]
                    cnt += 1
                    while dist[lidx] != before:
                        lidx -= 1
                else:
                    dist[ridx] = dist[lidx]
                    ridx += 1
                    cnt += 1
            else:
                ridx, lidx = ridx + 1, ridx
            if cnt > n:
                break
        if cnt > n:
            right = mid - 1
        else:
            left = mid
    return left