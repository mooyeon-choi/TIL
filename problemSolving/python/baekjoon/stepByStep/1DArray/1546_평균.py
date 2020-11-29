N = int(input())
scores = list(map(int, input().split()))
maxNum = max(scores)
for i in range(N):
  scores[i] *= 100 / maxNum / N
print(sum(scores))