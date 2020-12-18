H, M = map(int, input().split())

if M < 45:
  if H: 
    H -= 1
  else:
    H += 23 
  M += 15
else:
  M -= 45
  
print(H, M)