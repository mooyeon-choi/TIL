import sys
for _ in range(int(sys.stdin.readline())):
  n = int(sys.stdin.readline())
  location, next, time, check = 0, 0, 0, 0
  answer = 0
  for i in range(n):
    t, x = map(int, sys.stdin.readline().split())
    if t == check:
      answer += 1
      location, time = next, check
      next, check = x, abs(location - x) + t
    elif t > check:
      answer += 1
      location, time = next, t
      next, check = x, abs(location - x) + t
    else:
      print('check', location, time, next, check)
      if next < location:
        now = location - t - time
        if now >= x >= next:
          answer += 1
      elif next > location:
        now = location + t - time
        if next >= x >= now:
          answer += 1
      else:
        now = location
  print('answer', answer)