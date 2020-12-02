X = int(input())
now = 1
for i in range(X + 1):
  if now + i == X:
    print(f'1/{i + 1}')
    break
  elif now + i > X:
    if i % 2:
      print(f'{now + i - X}/{X - now + 1}')
    else:
      print(f'{X - now + 1}/{now + i - X}')
    break
  else:
    now += i