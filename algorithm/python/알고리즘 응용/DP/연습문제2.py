n = int(input())
left, right = 0, 0
for i in range(1, n + 1):
    if i == 1:
        left = 1
        right = 2
    else:
        left, right = right, right * 2 + left
print(right)