# while문

## 목차

* A+B-5
* A+B-4
* [더하기 사이클](#더하기-사이클)

## A+B-5

> 난이도 : Bronze III

* 문제

  두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

* 입력

  입력은 여러 개의 테스트 케이스로 이루어져 있다.

  각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

  입력의 마지막에는 0 두 개가 들어온다.

* 풀이

  ```python
  while True:
    A, B = map(int, input().split())
    if A or B:
      print(A + B)
    else:
      break
  ```

  * 기본적인 while문 사용법이다.
  * A, B 모두 0이 아닌경우 `print(A + B)`를 해주었다.

## A+B-4

> 난이도 : Bronze III

* 문제

  두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

* 입력

  입력은 여러 개의 테스트 케이스로 이루어져 있다.

  각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

* 풀이

  ```python
  while True:
    try:
      print(sum(map(int, input().split())))
    except:
      break
  ```

  ```python
  import sys
  for line in sys.stdin:
    print(sum(map(int, line.split())))
  ```

  * 두가지 풀이법이 있다.
  * Python `try exept` 를 사용하여 받을 입력이 없을 경우 `break`로 반복문을 종료할 수 있다.
  * `sys.stdin`을 통해 모든 입력을 한번에 받고 각 각의 입력에 대해서 A+B를 출력해줄 수 있다.

## 더하기 사이클

> Bronze I

* [문제링크](https://www.acmicpc.net/problem/1110)

* 입력

  첫째 줄에 N이 주어진다. N은 0보다 크거나 같고, 99보다 작거나 같은 정수이다.

* 풀이

  ```python
  N = int(input())
  memo = N
  answer = 0
  while True:
    answer += 1
    memo = (memo % 10) * 10 + (memo // 10 + memo % 10) % 10
    if memo == N:
      break
  print(answer)
  ```

  * N의 1의 자리수를 10의 자리에

  * (N의 10의 자리수 + N의 1의 자리수)의 1의 자리수

  * 위 두 조건을 수식으로 쓴다면 다음과 같다.

    `(N % 10) * 10 + (N // 10 + N % 10)% 10`

    이를 활용해서 간단하게 해결할 수 있다.

