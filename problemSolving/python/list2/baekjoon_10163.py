n = int(input())
background = [[0 for _ in range(101)] for _ in range(101)]
for num in range(1, n + 1):
    color_p = list(map(int, input().split()))
    for i in range(color_p[1], color_p[3] + color_p[1]):
        for j in range(color_p[0], color_p[2] + color_p[0]):
            background[i][j] = num
for num in range(1, n + 1):
    count = 0
    for i in range(101):
        for j in range(101):
            if background[i][j] == num:
                count += 1
    print(count)