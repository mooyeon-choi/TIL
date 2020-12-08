N = int(input())
people = []
tier = [1] * N
for _ in range(N):
  people.append(tuple(map(int, input().split())))
for i in range(N):
  for j in range(N):
    if i != j:
      if people[j][0] > people[i][0] and people[j][1] > people[i][1]:
        tier[i] += 1

print(' '.join(map(lambda x: str(x), tier)))