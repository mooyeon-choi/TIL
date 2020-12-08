N, M = map(int, input().split())
nums = list(map(int, input().split()))
answer = 0
for i in range(N):
  for j in range(i + 1, N):
    for k in range(j + 1, N):
      if nums[i] + nums[j] + nums[k] <= M:
        if M - answer > M - (nums[i] + nums[j] + nums[k]):
          answer = nums[i] + nums[j] + nums[k]
print(answer)