def solution(cookie):
    answer = 0
    for i in range(len(cookie) - 1):
        left, leftV = i, cookie[i]
        right, rightV = i + 1, cookie[i + 1]
        while (left >= 0 or leftV > rightV) and (right <= len(cookie) - 1 or rightV > leftV):
            if leftV == rightV:
                if answer < leftV:
                    answer = leftV
                if left > 0:
                    left -= 1
                    leftV += cookie[left]
                else:
                    break
            elif leftV < rightV:
                if left > 0:
                    left -= 1
                    leftV += cookie[left]
                else:
                    break
            else:
                if right < len(cookie) - 1:
                    right += 1
                    rightV += cookie[right]
                else:
                    break
    return answer