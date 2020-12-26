def dfs(node):
  preorder.append(node)
  if tree[node][0] != '.':
    dfs(tree[node][0])
  inorder.append(node)
  if tree[node][1] != '.':
    dfs(tree[node][1])
  postorder.append(node)

n = int(input())
tree = {}
preorder = []
inorder = []
postorder = []
for _ in range(n):
  a, b, c = input().split()
  tree[a] = [b, c]

dfs('A')

print(''.join(preorder))
print(''.join(inorder))
print(''.join(postorder))