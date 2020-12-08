# 재귀

## 목차

* [팩토리얼](#팩토리얼)
* [피보나치 수 5](#피보나치-수-5)
* [별 찍기 10](#별-찍기-10)
* [하노이 탑 이동 순서](#하노이 탑 이동 순서)

## 팩토리얼

> 난이도 : Bronze III

* 문제

  0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.

* 입력

  첫째 줄에 정수 N(0 ≤ N ≤ 12)가 주어진다.

* 풀이

  ```python
  def fac(N):
    if N < 2: return 1
    return N * fac(N - 1)
  
  print(fac(int(input())))
  ```

  * 기본적인 재귀함수의 사용법을 알아보는 문제였다.

  ```python
  answer = 1
  for i in range(1, int(input()) + 1):
    answer *= i
  print(answer)
  ```

  * 위와 같은 단순 반복문이 더 빠르고 재귀횟수를 초과할 걱정도 없어 입력값이 매우 커지면 더 안전하다.

## 피보나치 수 5

> 난이도 : Bronze II

* 풀이

  피보나치 수는 0과 1로 시작한다. 0번째 피보나치 수는 0이고, 1번째 피보나치 수는 1이다. 그 다음 2번째 부터는 바로 앞 두 피보나치 수의 합이 된다.

  이를 식으로 써보면 Fn = Fn-1 + Fn-2 (n ≥ 2)가 된다.

  n=17일때 까지 피보나치 수를 써보면 다음과 같다.

  0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597

  n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램을 작성하시오.

* 입력

  첫째 줄에 n이 주어진다. n은 20보다 작거나 같은 자연수 또는 0이다.

* 풀이

  ```python
  def fibo(n):
    if n < 1: return 0
    elif n == 1: return n
    return fibo(n - 1) + fibo(n - 2)
  
  print(fibo(int(input())))
  ```

  * `n`이 1이하인 경우에 주의하여 재귀함수를 작성하면 된다.

  ```python
  N = int(input())
  result = []
  for i in range(N + 1):
    if len(result) < 2:
      result.append(i)
    else:
      fibo1 = result.pop()
      fibo2 = result.pop()
      if i != N:
        result.append(fibo1)
      result.append(fibo1 + fibo2)
  else:
    print(result[-1])
  ```

  * 재귀함수는 스택 메모리 공간에서 동작한다. 따라서, 위와 같이 스택 자료구조를 활용해서도 풀 수 있다.

## 별 찍기 10

> 난이도 : Silver I

* 문제

  재귀적인 패턴으로 별을 찍어 보자. N이 3의 거듭제곱(3, 9, 27, ...)이라고 할 때, 크기 N의 패턴은 N×N 정사각형 모양이다.

  크기 3의 패턴은 가운데에 공백이 있고, 가운데를 제외한 모든 칸에 별이 하나씩 있는 패턴이다.

  ```
  ***
  * *
  ***
  ```

  N이 3보다 클 경우, 크기 N의 패턴은 공백으로 채워진 가운데의 (N/3)×(N/3) 정사각형을 크기 N/3의 패턴으로 둘러싼 형태이다. 예를 들어 크기 27의 패턴은 예제 출력 1과 같다.

* 입력

  첫째 줄에 N이 주어진다. N은 3의 거듭제곱이다. 즉 어떤 정수 k에 대해 N=3k이며, 이때 1 ≤ k < 8이다.

* 풀이

  ```python
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
  
  ```

  * List에 첫번째, 두번째, 세번째 줄 String을 저장하며 재귀로 구현하였다.

## 하노이 탑 이동 순서

> 난이도 : Silver II

* [문제 링크](https://www.acmicpc.net/problem/11729)

* 입력

  첫째 줄에 첫 번째 장대에 쌓인 원판의 개수 N (1 ≤ N ≤ 20)이 주어진다.

* 풀이

  ```python
  def hanoi(n, start, between, end):
    if n == 1:
      print(start, end)
      return
    hanoi(n - 1, start, end, between)
    print(start, end)
    hanoi(n - 1, between, start, end)
  
  N = int(input())
  print(2**N - 1)
  hanoi(N, 1, 2, 3)
  ```

  * 대표적인 재귀 문제이다.
  * 기본적인 규칙을 이해하고나면 간단하게 해결할 수 있다.

  풀이 방법

  * 옮겨야 할 블럭이 하나라면 바로 목적지로 옮겨준다.
  * 옮겨야 할 블럭이 2개 이상이라면
    * 블럭을 중간 지점에 잠깐 옮겨둔다
    * 아래의 블럭을 목적지로 옮긴다.
    * 중간 지점에 가져다둔 블럭을 다시 목적지로 옮긴다.

  