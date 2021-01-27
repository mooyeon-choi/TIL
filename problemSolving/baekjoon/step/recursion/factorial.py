# def fac(N):
#   if N < 2:
#     return 1
#   return N * fac(N - 1)


# print(fac(int(input())))

answer = 1
for i in range(1, int(input()) + 1):
  answer *= i
print(answer)