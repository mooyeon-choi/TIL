for _ in range(int(input())):
  n = int(input())
  word = input()
  if '2020' == word[-4:]:
    print('YES')
  elif '2' == word[0] and '020' == word[-3:]:
    print('YES')
  elif '20' == word[:2] and '20' == word[-2:]:
    print('YES')
  elif '202' == word[:3] and '0' == word[-1]:
    print('YES')
  elif '2020' == word[:4]:
    print('YES')
  else:
    print('NO')