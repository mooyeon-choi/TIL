# Class 4

> [Solved.ac](https://solved.ac/) Class 4 문제

## 목차

* [제곱 ㄴㄴ 수](#제곱-ㄴㄴ-수)
* [트리 순회](#트리-순회)
* [조합](#조합)
* [스티커](#스티커)

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