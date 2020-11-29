# for문

> python for문의 활용법을 익혀보자

## 목차

* [구구단](#구구단)
* [A+B-3](#A\+B-3)
* [합](#합)
* [빠른 A+B](#빠른-A\+B)

## 구구단

> 난이도 : Bronze III

* 문제

  N을 입력받은 뒤, 구구단 N단을 출력하는 프로그램을 작성하시오. 출력 형식에 맞춰서 출력하면 된다.

* 입력

  첫째 줄에 N이 주어진다. N은 1보다 크거나 같고, 9보다 작거나 같다.

* 풀이

  ```python
  N = int(input())
  for i in range(1, 10):
    print(N, '*', i, '=', N * i)
  ```

  * 기본적인 for문 사용법을 물어보는 문제였다.
  * `print()`에 `,`(콤마)를 사용하면 한칸 띄어서 출력된다.

## A+B-3

> 난이도 : Bronze III

* 문제

  두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

* 입력

  첫째 줄에 테스트 케이스의 개수 T가 주어진다.

  각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

* 풀이

  ```python
  T = int(input())
  for _ in range(T):
    print(sum(map(int, input().split())))
  ```

  * 여러줄의 입력을 for문을 사용해 받아보는 문제였다.

## 합

> 난이도 : Bronze V

* 문제

  n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.

* 입력

  첫째 줄에 n (1 ≤ n ≤ 10,000)이 주어진다.

* 풀이

  ```python
  N = int(input())
  answer = 0
  for i in range(1, N + 1):
      answer += i
  print(answer)
  ```

  ```python
  N = int(input())
  print((N + 1) * N // 2)
  ```

  * 기본적인 for문과 `range()` 를 활용해서 숫자를 더하는 문제였다.
  * 수학공식을 사용할 경우 시간복잡도가 O(1)으로 for문으로 풀 경우 시간복잡도가 O(n)이 되는 것보다 효율적으로 풀 수 있다.

## 빠른 A+B

> 난이도 Bronze II

* [문제 링크](https://www.acmicpc.net/problem/15552)

* 입력

  첫 줄에 테스트케이스의 개수 T가 주어진다. T는 최대 1,000,000이다. 다음 T줄에는 각각 두 정수 A와 B가 주어진다. A와 B는 1 이상, 1,000 이하이다.

* 풀이

  ```python
  import sys
  
  T = int(input())
  for _ in range(T):
    print(sum(map(int, sys.stdin.readline().rstrip().split())))
  ```

  * `sys.stdin` 를 활용하면 더 빠르게 입력을 받을 수 있다.
  * 대부분 코테의 경우 `input()` 만 사용하여도 되도록 문제를 출제하기 때문에 많이 사용하지는 않는다.
  * `sys.stdout` 은 사용해보았지면 별로 차이가 없어 그냥 `print()`를 사용해주었다.
  * 이 문제의 경우 `sys.stdin.read()`로 한번에 받아온 후 `\n` 과 `' '`로 나눠주면 실행시간을 더 줄일 수 있다.

## N 찍기

> 난이도 : Bronze III

* 문제

  자연수 N이 주어졌을 때, 1부터 N까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.

* 입력

  첫째 줄에 100,000보다 작거나 같은 자연수 N이 주어진다.

* 풀이

  ```python
  N = int(input())
  for i in range(1, N + 1):
    print(i)
  ```

  * for문의 기본적인 사용법을 묻는 간단한 문제였다.

## 기찍 N

> 난이도 : Bronze III

* 문제

  자연수 N이 주어졌을 때, N부터 1까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.

* 입력

  첫째 줄에 100,000보다 작거나 같은 자연수 N이 주어진다.

* 풀이

  ```python
  N = int(input())
  for i in range(N, 0, -1):
    print(i)
  ```

  * `range(a, b, c)` 로 입력할 경우 `a` 에서부터 `b`이 되기 전까지 `c` 만큼 값을 변화시키며 반복된다.

## A+B-7

> 난이도 : Bronze III

* 문제

  두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

* 입력

  첫째 줄에 테스트 케이스의 개수 T가 주어진다.

  각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

* 풀이

  ```python
  T = int(input())
  for TC in range(1, T + 1):
    print(f'Case #{TC}: {sum(map(int, input().split()))}')
  ```

  * python `F-string` 을 활용하여 `f"string {변수}"` 와 같이 입력 할 수 있다.

## A+B-8

> 난이도 : Bronze III

* 문제

  두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

* 입력

  첫째 줄에 테스트 케이스의 개수 T가 주어진다.

  각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

* 풀이

  ```python
  T = int(input())
  for TC in range(1, T + 1):
    A, B = map(int, input().split())
    print(f'Case #{TC}: {A} + {B} = {A + B}')
  ```

  * 이전 문제와 같은 방법으로 풀 수 있다.

## 별찍기-1

> 난이도 : Bronze III

* 문제

  첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제

* 입력

  첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

* 풀이

  ```python
  N = int(input())
  for i in range(1, N + 1):
    print('*' * i)
  ```

  * `"string"` * `integer` 의 경우 `"string"` 을 `integer` 값 만큼 반복해서 붙여준다.

## 별찍기-2

> 난이도 : Bronze III

* 문제

  첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제

  하지만, 오른쪽을 기준으로 정렬한 별(예제 참고)을 출력하시오.

* 입력

  첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

* 풀이

  ```python
  N = int(input())
  for i in range(1, N + 1):
    print(' ' * (N - i) + '*' * i)
  ```

  * `"string"` + `"string"` 으로 두개의 string을 연결해 줄 수 있다.

## X보다 작은 수

> 난이도 : Bronze III

* 문제

  정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.

* 입력

  첫째 줄에 N과 X가 주어진다. (1 ≤ N, X ≤ 10,000)

  둘째 줄에 수열 A를 이루는 정수 N개가 주어진다. 주어지는 정수는 모두 1보다 크거나 같고, 10,000보다 작거나 같은 정수이다.

* 풀이

  ```python
  N, X = map(int, input().split())
  result = []
  for num in input().split():
      if int(num) < X:
          result.append(num)
  print(' '.join(result))
  ```

  ```python
  N, X = map(int, input().split())
  A = filter(lambda x: int(x) < X, input().split())
  print(' '.join(A))
  ```

  ```python
  N, X = map(int, input().split())
  A = [num for num in input().split() if int(num) < X]
  print(' '.join(A))
  ```

  * 다양한 방법으로 풀 수 있다
  * 먼저 첫번째 방법은 가장 기본적인 for문과 if문을 활용한 방법이다. `result` list를 만들어주고 정수가 X 보다 작을때 `append()` 해준다.
  * `filter()` 와 `lambda` 를 활용한 방법이다. `filter()` 를 통해 주어진 함수에서 true인 값만 `A`에 넣어준다. 이때 `lambda`를 활용하면 간단한 함수를 구현할 수 있다.
  * Generator expressions 를 활용한 방법이다. Python으로 코딩테스트를 준비할 경우 사용법을 익혀두면 많은 곳에서 유용하게 쓸 수 있다.

