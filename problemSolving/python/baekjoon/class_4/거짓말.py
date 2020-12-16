N, M = map(int, input().split())
know, *knowSet = map(int, input().split())
knowSet = set(knowSet)
tree = [set() for i in range(N + 1)];
for _ in range(M):
  person, *perSet = map(int, input().split())
  for i in range(len(perSet)):
    tree[perSet[i]] |= set(perSet)

known = set()
def 
for num in knowSet:
  