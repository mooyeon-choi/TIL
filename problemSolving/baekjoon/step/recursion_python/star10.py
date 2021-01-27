def draw(n):
  if n == 1:
    return ['*']
  else:
    beforelist = draw(n//3)
    newlist = []
    for i in range(3):
      if i != 1:
        for j in range(len(beforelist)):
          newlist.append(beforelist[j] * 3)
      else:
        for j in range(len(beforelist)):
          newlist.append(beforelist[j] + ' '*(n//3) + beforelist[j])
    return newlist

print('\n'.join(draw(int(input()))))
