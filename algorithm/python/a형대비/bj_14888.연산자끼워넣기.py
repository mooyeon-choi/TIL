def back(num, count):
    if count == n:
        result.append(num)
        return
    else:
        for i in range(4):
            if operator[i]:
                operator[i] -= 1
                if i == 0:
                    nxt = num + numbers[count]
                    back(nxt, count + 1)
                elif i == 1:
                    nxt = num - numbers[count]
                    back(nxt, count + 1)
                elif i == 2:
                    nxt = num * numbers[count]
                    back(nxt, count + 1)
                elif i == 3:
                    if num > 0:
                        nxt = num // numbers[count]
                        back(nxt, count + 1)
                    elif num <= 0:
                        nxt = -(abs(num) // numbers[count])
                        back(nxt, count + 1)
                operator[i] += 1

n = int(input())
result = []
numbers = list(map(int, input().split()))
operator = list(map(int, input().split()))
back(numbers[0], 1)
print(max(result))
print(min(result))