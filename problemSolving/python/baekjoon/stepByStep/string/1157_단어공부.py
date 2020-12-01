word = input().upper()
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
maxStr, maxCnt = '?', 0
for alpha in alphabet:
  cnt = word.count(alpha)
  if cnt > maxCnt:
    maxStr, maxCnt = alpha, cnt
  elif cnt == maxCnt:
    maxStr = '?'
print(maxStr)