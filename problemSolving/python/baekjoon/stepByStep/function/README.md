# 함수

> Python에서 Function을 구현해보자

## 목차

* [정수 N개의 합](#정수-n개의-합)
* [셀프 넘버](#셀프-넘버)
* [한수](#한수)

## 정수 N개의 합

> 난이도 : Bronze II

* 문제

  정수 n개가 주어졌을 때, n개의 합을 구하는 함수를 작성하시오.

  작성해야 하는 함수는 다음과 같다.

* 입력

  `def solve(a: list)`

  `a`: 합을 구해야 하는 정수 `n`개가 저장되어 있는 리스트 (0 ≤ a[i] ≤ 1,000,000, 1 ≤ n ≤ 3,000,000)

* 풀이

  ```python
  def solve(a):
    return sum(a)
  ```

  * Python에서는 함수의 매개 변수, 리턴 값의 자료형을 알아서 처리해주므로 따로 입력해주지 않아도 된다.

## 셀프 넘버

> 난이도 : Bronze I

* [문제 링크](https://www.acmicpc.net/problem/4673)

* 입력

  없음

* 풀이

  ```python
  def plus(num):
    for n in str(num):
      num += int(n)
    if num > 10000:
      return
    numList[num] = 0
  
  numList = [1] * 10001
  for i in range(1, 10001):
    plus(i)
  for i in range(1, 10001):
    print(i) if numList[i] else None
  ```

  * 함수안에서는 글로벌 변수의 값을 바꿔줄 수 없다.
  * 하지만, List의 경우 변수에 리스트의 주소값만 저장되어 있으므로 내부의 값들을 바꿔줄 수 있다.

## 한수

> 난이도 : Silver IV

* 문제

  어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다. 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다. N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오. 

* 입력

  첫째 줄에 1,000보다 작거나 같은 자연수 N이 주어진다.

* 풀이

  ```python
  def check(num):
    if int(num) > 99:
      between = int(num[0]) - int(num[1])
      for i in range(1, len(num) - 1):
        if between != int(num[i]) - int(num[i + 1]):
          return False
    return True
  
  N = int(input())
  answer = 0
  for i in range(1, N + 1):
    answer += check(str(i))
  print(answer)
  ```

  * 99까지는 모두 한수이므로 99가 넘는 숫자에 대해서만 검증을 한다.
  * `Integer + Boolean` 계산시 Boolean `True` 는 Integer `1`, `False` 는 `0`으로 계산된다.

