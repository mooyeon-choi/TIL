for _ in range(int(input())):
  chars = input()
  if len(chars) & 1:
    print('NO')
  else:
    rcnt = 0
    lcnt = 0
    for i in range(len(chars)):
      if chars[i] == ')':
        rcnt += 1
        if rcnt > (i + 1) // 2:
          print('NO')
          break
      if chars[len(chars) - 1 - i] == '(':
        lcnt += 1
        if lcnt > (i + 1) // 2:
          print('NO')
          break
    else:
      print('YES')
