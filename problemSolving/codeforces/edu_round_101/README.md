# Educational Codeforces Round 101 (Rated for Div. 2)

## 목차

* [A Regular Bracket Sequence](#a-regular-bracket-sequence)
* [B Red and Blue](#b-red-and-blue)
* [C Building a Fence](#c-building-a-fence)

## A Regular Bracket Sequence

* [문제 링크](https://codeforces.com/contest/1469/problem/A)

* 1번 문제치곤 조금 까다로운 문제였다.

* 모든 괄호가 짝을 이룰 수 있는지 확인하는 문제였다.

* 풀이

  ```python
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
  
  ```

  * 왼쪽에서부터 `)`를 확인했을 때 `현재 인덱스 위치 + 1 // 2` 보다 `)`의 갯수가 적을 경우 나머지는 `?`나 `(` 가 되므로 `)`와 모두 짝을 이뤄 줄 수 있다.
  * 마찬가지로 오른쪽에서부터 `(`를 확인한다.
  * 양쪽 모두 가능하면 `YES`를 리턴하고, 어느 하나라도 안되는게 있으면 `NO`를 리턴한다.
  * 홀수일경우 `NO`를 리턴한다.

## B Red and Blue

* [문제 링크](https://codeforces.com/contest/1469/problem/B)

* Red 색상을 가진 리스트, Blue 색상을 가진 리스트가 입력으로 들어 온다.

* 두 리스트를 각각의 index 순서는 유지하면서 섞어준다.

  ex) `[R1, R2, B1, B2, R3, B3, R4] or [B1, R1, R2, B2, R3, B3, R4]`

* 만들 수 있는 리스트들로 0 ~ n번째 인덱스 까지의 합을 구하며 합이 가장 클 때를 찾아 출력한다.

* 풀이

  ```python
  for _ in range(int(input())):
    n = int(input())
    nnums = list(map(int, input().split()))
    m = int(input())
    mnums = list(map(int, input().split()))
    nmax = 0
    mmax = 0
    cnt = 0
    for num in nnums:
      cnt += num
      if cnt > nmax:
        nmax = cnt
    cnt = 0
    for num in mnums:
      cnt += num
      if cnt > mmax:
        mmax = cnt
    print(nmax + mmax)
  ```

  * Red, Blue 각각의 리스트에서 최대값을 구한 후 더해주면 되는 문제였다.

## C Building a Fence

* [문제 링크](https://codeforces.com/contest/1469/problem/C)

* 높이가 `k` 너비가 `1`인 벽이있다.

* 양쪽 맨 끝의 벽은 항상 바닥과 붙어있다.

* 서로 인접한 벽들은 길이가 1이상 맞닿아 있어야한다.

* 이때 입력으로 들어오는 지형에 이 벽이 안 끊어지게 세울 수 있는지 찾아보는 문제였다.

* 풀이

  ```python
  import sys
  
  for _ in range(int(input())):
    n, k = map(int, sys.stdin.readline().split())
    heights = list(map(int, sys.stdin.readline().split()))
    memo = [[0, 0] for __ in range(n)]
    for i in range(n):
      if not i:
        memo[0][0] = heights[i] + 1
        memo[0][1] = heights[i] + k - 1
      elif i <= n - 2:
        if memo[i-1][1] >= heights[i] >= memo[i-1][0] - 2 * k + 1:
          memo[i][1] = min(memo[i-1][1] + k - 1, heights[i] + 2*k - 2)
          memo[i][0] = max(0, memo[i-1][0] - k + 1, heights[i] + 1)
        else:
          print('NO')
          break
      else:
        if memo[i-1][1] >= heights[i] >= memo[i-1][0] - k:
          print('YES')
        else:
          print('NO')
          break
      print(memo)
  ```

  * 먼저 입력으로 받아야할 값의 수가 많아 `sys.stdin.readline()`으로 입력값을 받아주었다.
  * DP로 풀며 메모이제이션에 이전 벽에서 최대로 높게 지을 수 있는 높이, 최소 높이를 전달하며 현재 위치에서 벽을 지을 수 있는지 확인해주었다.
  * 마지막 위치에서는 항상 바닥에 붙어있어야 하므로 바닥에 붙게 벽을 세울 수 있는지 확인해주었다.
  * 모든 벽을 정상적으로 건설 할 수 있으면 `YES` 중간에 끊기거나 마지막 위치의 벽을 건설 할 수 없으면 `NO` 를 출력해 주었다.