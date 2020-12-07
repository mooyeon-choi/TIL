location = [int(input()) for _ in range(2)]
print((1 if location[0] > 0 else 2) if location[1] > 0 else (4 if location[0] > 0 else 3))