# Codeforces Round #689 (Div. 2, based on Zed Code Competition)

> 간단한 문제도 헤매다가 못풀고 3번 문제는 뭐라는건지 이해도 안되고.... 아쉬움이 많은 대회였다.

## 목차

* [A String Generation](#a-string-generation)
* [B Find the Spruce](#b-find-the-spruce)
* [D Divide and Summarize](#d-divide-and-summarize)

## A String Generation

* [문제 링크](https://codeforces.com/contest/1461/problem/A)

* 가장큰 palindrome substring의 길이가 K 이하가 되도록 `a, b, c` 문자를 사용해 길이가 N인 문자열을 만드는 문제였다.

* 풀이

  ```python
  string = ['a', 'b', 'c']
  for _ in range(int(input())):
    N, K = map(int, input().split())
    word = ''
    idx = 0
    while len(word) < N:
      if len(word) + K < N:
        word = word + string[idx % 3]*K
      else:
        word = word + string[idx % 3] * (N - len(word))
      idx += 1
    print(word)
  ```

  * 단순히 `a`, `b`, `c` 순서대로 K개씩 연결해주며 길이가 N인 문자열을 만들어주었다.
  * 항상 `abca`, `aabbccaa` 형태로 만들어지므로 가장 긴 팰린드롬 형태의 substring은 `a` * K, `b` * K, `c` * K 가 될 것이다. 

## B Find the Spruce

* [문제 링크](https://codeforces.com/contest/1461/problem/B)

* `input`으로 들어오는 `.`, `*` 로 이루어진 행렬에서 `*` 로 만들 수 있는 정삼각형 모양의 갯수를 찾는 문제였다.

* 풀이

  ```python
  for _ in range(int(input())):
    N, M = map(int, input().split())
    board = [input() for __ in range(N)]
    visit = [[0]*M for __ in range(N)]
    answer = 0
    for i in range(N - 1, -1, -1):
      for j in range(M):
        if board[i][j] == '*':
          if i == N - 1:
            visit[i][j] = 1
          else:
            if M - 1 > j and j > 0:
              visit[i][j] = 1 + min(visit[i + 1][j - 1], visit[i + 1][j], visit[i + 1][j + 1])
            else:
              visit[i][j] = 1
    print(sum(map(sum, visit)))
  ```

  * 문제를 읽어보면 바로 DP로 풀어야 하는 문제임을 알 수 있다.

    메모이제이션을 어떻게 해줄지 생각하며 접근하였다.

  * `*`의 위치에 현재 위치를 위쪽 꼭지점으로 가지는 정삼각형의 갯수를 저장한다면 

    `(i + 1, j - 1), (i + 1, j), (i + 1, j + 1)` 위치에서 만들 수 있는 갯수의 최솟값 + 1 만큼있다.

    따라서 아래에서 위로 올라가며 갯수를 저장해주고 모두 더해주는 방식으로 풀었다.

## D Divide and Summarize

* [문제 링크](https://codeforces.com/contest/1461/problem/D)

* `(max + min) / 2` 값을 기준으로 배열을 계속 나눠주며 만들 수 있는 부분집합 원소의 합을 저장해주고 입력받은 숫자가 여기에 속하는지 찾는 문제였다.

* 풀이

  ```python
  def find(num):
    if not num:
      return
    elif len(set(num)) == 1:
      result.add(sum(num))
      return
    result.add(sum(num))
    mid = (num[0] + num[-1]) / 2
    for i in range(len(num) - 1, -1, -1):
      if num[i] <= mid:
        find(num[:i+1])
        find(num[i+1:])
        return
  
  for _ in range(int(input())):
    n, q = map(int, input().split())
    nums = sorted(list(map(int, input().split())))
    result = set()
    find(nums)
    for __ in range(q):
      print('Yes' if int(input()) in result else 'No')
  ```

  * 2000ms 제한 문제에서 1950ms로 간신히 통과했다.

    다른 더 효율성이 좋은 방법도 있을 것 같다.

  * 재귀함수를 통해 리스트를 계속해서 `mid` 기준으로 나눠주며 `sum(list)`의 값을 저장하였다. 