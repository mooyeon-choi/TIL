N = int(input())
memo = [0, 0, 0]
for _ in range(N):
  nums = list(map(int, input().split()))
  nums[0] += min(memo[1], memo[2])
  nums[1] += min(memo[0], memo[2])
  nums[2] += min(memo[0], memo[1])
  memo = nums
print(min(nums))
