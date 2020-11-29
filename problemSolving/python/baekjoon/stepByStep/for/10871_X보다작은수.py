N, X = map(int, input().split())
A = [num for num in input().split() if int(num) < X]
print(' '.join(A))