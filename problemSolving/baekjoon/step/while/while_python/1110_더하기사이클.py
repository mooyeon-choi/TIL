N = input()
memo = N
answer = 0
while True:
  answer += 1
  new = sum([int(num) for num in memo])
  memo = memo[-1] + str(new)[-1]
  if int(memo) == int(N):
    break
print(answer)