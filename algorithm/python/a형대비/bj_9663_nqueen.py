def back(count):
    global answer
    now = list(cant)
    if count == n + 1:
        answer += 1
        return
    else:
        for i in range(n):
            if cant[i]:
                if i + (count - cant[i]) < n:
                    now[i + (count - cant[i])] = 1
                if i - (count - cant[i]) >= 0:
                    now[i - (count - cant[i])] = 1
        for i in range(n):
            if not now[i]:
                cant[i] = count
                back(count + 1)
                cant[i] = 0
        else:
            return

answer = 0
n = int(input())
cant = [0]*n
back(1)
print(answer)