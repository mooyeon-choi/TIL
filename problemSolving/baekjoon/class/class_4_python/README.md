# Class 4

> [Solved.ac](https://solved.ac/) Class 4 문제

## 목차

* [제곱 ㄴㄴ 수](#제곱-ㄴㄴ-수)
* [트리 순회](#트리-순회)
* [조합](#조합)
* [스티커](#스티커)
* [N과 M(8)](#n과-m8)
* [N과 M(9)](#n과-m9)

## 제곱 ㄴㄴ 수

* 문제

  어떤 수 X가 1보다 큰 제곱수로 나누어 떨어지지 않을 때, 제곱ㄴㄴ수라고 한다. 제곱수는 정수의 제곱이다. min과 max가 주어지면, min과 max를 포함한 사이에 제곱ㄴㄴ수가 몇 개 있는지 출력한다.

* 입력

  첫째 줄에 min과 max가 주어진다. min은 1보다 크거나 같고, 1,000,000,000,000보다 작거나 같은 자연수이고, max는 min보다 크거나 같고, min+1,000,000보다 작거나 같은 자연수이다.

* 풀이

  ```python
  n, m = map(int, input().split())
  answer = 0
  result = set(range(n, m + 1))
  for i in range(2, int(m**(1/2)) + 1):
    for j in range(n//i**2, m//i**2 + 1):
      if i**2 * j in result:
        result.remove(i**2 * j)
  print(len(result))
  ```

  * 2 ~ m<sup>(1/2)</sup> 까지의 숫자의 제곱을 n / i<sup>2</sup> ~ m / i<sup>2</sup> 까지의 수로 곱해주면 원하는 범위의 제곱수(제곱 ㄴㄴ 수의 반대)를 찾을 수 있다
  * `result` Set에서 제곱수들을 지워주고 남은 크기를 출력하였다.

## 트리 순회

* [문제 링크](https://www.acmicpc.net/problem/1991)

* 풀이

  ```python
  def dfs(node):
    preorder.append(node)
    if tree[node][0] != '.':
      dfs(tree[node][0])
    inorder.append(node)
    if tree[node][1] != '.':
      dfs(tree[node][1])
    postorder.append(node)
  
  n = int(input())
  tree = {}
  preorder = []
  inorder = []
  postorder = []
  for _ in range(n):
    a, b, c = input().split()
    tree[a] = [b, c]
  
  dfs('A')
  
  print(''.join(preorder))
  print(''.join(inorder))
  print(''.join(postorder))
  ```

  * DFS의 node를 출력해주는 시점을 통해 Preorder, Inorder, Postorder Traversal로 구분된다.

## 조합

* [문제 링크](https://www.acmicpc.net/problem/2407)

* 풀이

  ```python
  def dfs(num, cnt):
    if cnt == m:
      return num
    else:
      return num * dfs(num - 1, cnt + 1)
  
  n, m = map(int, input().split())
  print(dfs(n, 1) // dfs(m, 1))
  ```

  * 최대 반복횟수가 100이므로 재귀함수를 사용하여도 recursion depth error가 발생하지 않을 것이다.
  * 따라서 재귀함수를 사용하여 간단하게 풀 수 있다.

## 스티커

* [문제 링크](https://www.acmicpc.net/problem/9465)

* 풀이

  ```python
  for _ in range(int(input())):
    n = int(input())
    board = [list(map(int, input().split())) for __ in range(2)]
    for i in range(1, n):
      if i == 1:
        board[0][i] += board[1][i - 1]
        board[1][i] += board[0][i - 1]
      else:
        board[0][i] += max(board[1][i - 1], board[1][i - 2])
        board[1][i] += max(board[0][i - 1], board[0][i - 2])
    print(max(board[0][-1], board[1][-1]))
  ```

  * DP로 풀 수 있는 문제였다.
  * 현재 위치를 `i` 라 할 때 반대편 위치의 `i - 1`, `i - 2`번째 값중 큰값을 더해주며 진행하면 된다.

## N과 M(8)

* [문제 링크](https://www.acmicpc.net/problem/15657)

* 풀이

  ```python
  def dfs(idx, cnt, result):
    if cnt == m:
      print(' '.join(result))
      return
    else:
      for i in range(idx, n):
        dfs(i, cnt + 1, result + [str(nums[i])])
  
  n, m = map(int, input().split())
  nums = sorted(list(map(int, input().split())))
  dfs(0, 0, [])
  ```

  * 먼저 입력받은 숫자들을 정렬해주고 재귀함수를 통해 현재 위치에서 마지막까지 반복문을 통해 풀면 되는 문제였다.

## N과 M(9)

* [문제 링크](https://www.acmicpc.net/problem/15663)

* 풀이

  ```python
  def dfs(idx, cnt, result):
    if cnt == m:
      if tuple(result) not in used:
        print(*result)
        used.add(tuple(result))
      return
    else:
      for i in range(0, n):
        if i not in idx:
          dfs(idx | {i}, cnt + 1, result + [nums[i]])
  
  n, m = map(int, input().split())
  used = set()
  nums = sorted(list(map(int, input().split())))
  dfs(set(), 0, [])
  ```

  * 똑같은 결과를 출력하면 안되므로 `set()`을 활용하여 used를 체크해주었다.
  * 마찬가지로 이미 사용한 index는 idx Set에 넣어주어 used 체크를 해주었다.

