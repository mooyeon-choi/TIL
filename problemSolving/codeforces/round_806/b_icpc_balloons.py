for _ in range(int(input())):
  num = int(input())
  string = input()
  check = set()
  answer = 0
  for i in string:
    if i in check:
      answer += 1
    else:
      check.add(i)
      answer += 2
  print(answer)