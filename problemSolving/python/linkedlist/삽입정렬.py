arr = [69, 10, 30, 2, 16, 8, 31, 22]
N = len(arr)
# 삽입하는 작업을 n-1번 반복 (1번 ~ n-1번)

for i in range(1, N):
    while i - 1 >= 0 and arr[i-1] > arr[i]:
        arr[i], arr[i-1] = arr[i-1], arr[i]

print(arr)