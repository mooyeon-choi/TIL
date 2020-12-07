# 수학 2

> 수식을 써서 효율적으로 풀 수 있는 문제들을 알아보자

## 목차

* [소수 찾기](#소수-찾기)
* [소수](#소수)
* [소수 구하기](#소수-구하기)
* [베르트랑 공준](#베르트랑-공준)
* [골드바흐의 추측](#골드바흐의-추측)
* [직사각형에서 탈출](#직사각형에서-탈출)
* [네 번째 점](#네-번째-점)
* [직각삼각형](#직각삼각형)
* [택시 기하학](#택시-기하학)
* [터렛](#터렛)

## 소수 찾기

> 난이도 : Silver IV

* 문제

  주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

* 입력

  첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

* 풀이

  ```python
  N = int(input())
  answer = 0
  for num in map(int, input().split()):
    if num > 1:
      for i in range(2, int(num**0.5) + 1):
        if not num % i:
          break
      else:
        answer += 1
  print(answer)
  ```

  * 16의 약수를 생각해보면 `1 * 16, 2 * 8, 4 * 4` 와 같이 나온다.

    따라서, `2`로 나눠진다면 `8` 도 뒤에 따라온다는 것을 알 수 있고 이러한 방식으로 `sqrt(16)` 까지만 확인한다면 모든 약수를 찾을 수 있다.

## 소수

> 난이도 : Silver IV

* 문제

  자연수 M과 N이 주어질 때 M이상 N이하의 자연수 중 소수인 것을 모두 골라 이들 소수의 합과 최솟값을 찾는 프로그램을 작성하시오.

  예를 들어 M=60, N=100인 경우 60이상 100이하의 자연수 중 소수는 61, 67, 71, 73, 79, 83, 89, 97 총 8개가 있으므로, 이들 소수의 합은 620이고, 최솟값은 61이 된다.

* 입력

  입력의 첫째 줄에 M이, 둘째 줄에 N이 주어진다.

  M과 N은 10,000이하의 자연수이며, M은 N보다 작거나 같다.

* 풀이

  ```python
  M = int(input())
  N = int(input())
  numSet = set()
  for num in range(M, N + 1):
    if num > 1:
      for i in range(2, int(num**0.5) + 1):
        if not num % i:
          break
      else:
        numSet.add(num)
  if numSet:
    print(sum(numSet))
    print(min(numSet))
  else:
    print(-1)
  ```

  * 위의 문제와 같은 방법으로 반복문에 넣어 풀어주었다.

## 소수 구하기

> 난이도 : Silver II

* 문제

  M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

* 입력

  첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.

* 풀이

  ```python
  M, N = map(int, input().split())
  for num in range(M, N + 1):
  if num > 1:
      for i in range(2, int(num**0.5) + 1):
        if not num % i:
          break
      else:
        print(num)
  ```
  
  ```python
  m, n = map(int, input().split())
  li = [False] + [True] * ((n - 1) // 2)
  for x in range(1, int(n**.5/2+1)):
    if li[x]:
      li[2*x*(x+1)::x*2+1] = [False] * ((((n + 1) // 2) - x * x * 2) // (x * 2 + 1))
  if m <= 2:
    print(2)
  print('\n'.join([f'{x}' for x, val in zip(range(m+(m&1==0), n+1, 2), li[m//2:]) if val]))
  ```
  
  