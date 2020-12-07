# 수학 1

> 분명 난이도는 낮은데 나한텐 너무 어렵다
>
> 역시 수학은 나랑 안맞아...

## 목차

* [손익분기점](#손익분기점)
* [설탕 배달](#설탕-배달)
* [벌집](#벌집)
* [분수찾기](#분수찾기)
* [달팽이는 올라가고 싶다](#달팽이는-올라가고-싶다)
* [ACM 호텔](#acm-호텔)
* [부녀회장이 될테야](#부녀회장이-될테야)
* [Fly me to the Alpha Centauri](#fly-me-to-the-alpha-centauri)

## 손익분기점

> 난이도 : Bronze IV

* [문제 링크](https://www.acmicpc.net/problem/1712)

* 입력

  첫째 줄에 A, B, C가 빈 칸을 사이에 두고 순서대로 주어진다. A, B, C는 21억 이하의 자연수이다.

* 풀이

  ```python
  import math
  
  A, B, C = map(int, input().split())
  if B >= C:
    print(-1)
  else:
    print(math.trunc(A/(C - B)) + 1)
  ```

  * math 모듈의 `ceil()`를 사용해 올림, `trunc()` 를 사용해 내림을 할 수 있다.
  * 처음으로 이익이 나는 때를 찾는 문제이므로 소수점 아래를 버리고 `+1`을 해서 찾아주었다.

## 설탕 배달

> 난이도 : Bronze I

* [문제 링크](https://www.acmicpc.net/problem/2839)

* 입력

  첫째 줄에 N이 주어진다. (3 ≤ N ≤ 5000)

* 풀이

  ```python
  N = int(input())
  for i in range(N//5, -1, -1):
    if not (N - 5 * i) % 3:
      print(i + (N - 5 * i) // 3)
      break
  else:
    print(-1)
  ```

  * `for else` 를 사용하면 for문이 중간에 끊기는곳 없이 모두 실행되었다면 else문을 실행한다.
  * 5킬로그램의 갯수가 가장 많을 때가 최소이므로 5킬로그램 봉지의 최대갯수에서 시작해서 딱 맞아 떨어질 때 반복문을 멈춰주면 된다.

## 벌집

> 난이도 : Bronze II

* [문제 링크](https://www.acmicpc.net/problem/2292)

* 입력

  첫째 줄에 N(1 ≤ N ≤ 1,000,000,000)이 주어진다.

* 문제

  ```python
  import math
  
  N = int(input())
  print(1 + math.ceil(((-1 + math.sqrt(4/3*N - 1/3)) / 2)))
  ```

  * 등차수열의 합 공식과 근의 공식을 사용해 수식을 만들 수 있다.

## 분수찾기

> 난이도 : Bronze II

* [문제 링크](https://www.acmicpc.net/problem/1193)

* 입력

  첫째 줄에 X(1 ≤ X ≤ 10,000,000)가 주어진다.

* 풀이

  ```python
  X = int(input())
  now = 1
  for i in range(X + 1):
    if now + i == X:
      if i % 2:
        print(f'1/{i + 1}')
      else:
        print(f'{i + 1}/1')
      break
    elif now + i > X:
      if i % 2:
        print(f'{now + i - X}/{X - now + 1}')
      else:
        print(f'{X - now + 1}/{now + i - X}')
      break
    else:
      now += i
  ```

  ```python
  # wnsqlehlswk님의 풀이
  k = int(input())
  n = 1
  while k > n:
      k, n = k - n, n + 1
  a, b = k, n - k + 1
  if n % 2 == 1:
      a, b = b, a
  print(str(a) + "/" + str(b))
  ```

  * 공식은 모르겠고.. 한줄한줄 다 찾으며 풀어주었다.
  * 다른 사람의 풀이를 보니 처음 입력받은 숫자를 등차수열로 빼주고 나머지, 현재 줄의 숫자 개수로 써서 풀면 간단하게 풀렸다.

## 달팽이는 올라가고 싶다

> 난이도 : Bronze II

* 문제

  땅 위에 달팽이가 있다. 이 달팽이는 높이가 V미터인 나무 막대를 올라갈 것이다.

  달팽이는 낮에 A미터 올라갈 수 있다. 하지만, 밤에 잠을 자는 동안 B미터 미끄러진다. 또, 정상에 올라간 후에는 미끄러지지 않는다.

  달팽이가 나무 막대를 모두 올라가려면, 며칠이 걸리는지 구하는 프로그램을 작성하시오.

* 입력

  첫째 줄에 세 정수 A, B, V가 공백으로 구분되어서 주어진다. (1 ≤ B < A ≤ V ≤ 1,000,000,000)

* 풀이

  ```python
  import math
  A, B, V = map(int, input().split())
  print(math.ceil((V - A) / (A - B)) + 1)
  ```

  * 마지막에는 올라간 후 바로 끝나므로 전체 높이에서 한번 올라가는 높이만큼 빼준 후 `하루동안 올라가는 높이 - 미끄러지는 높이` 로 나눠주고 `+1`을 해준다. 

## ACM 호텔

> 난이도 : Bronze III

* [문제 링크](https://www.acmicpc.net/problem/10250)

* 입력

  프로그램은 표준 입력에서 입력 데이터를 받는다. 프로그램의 입력은 T 개의 테스트 데이터로 이루어져 있는데 T 는 입력의 맨 첫 줄에 주어진다. 각 테스트 데이터는 한 행으로서 H, W, N, 세 정수를 포함하고 있으며 각각 호텔의 층 수, 각 층의 방 수, 몇 번째 손님인지를 나타낸다(1 ≤ H, W ≤ 99, 1 ≤ N ≤ H × W). 

* 풀이

  ```python
  import math
  for _ in range(int(input())):
    H, W, N = map(int, input().split())
    Y = str(N % H) if N % H else str(H)
    X = str(math.ceil(N / H)) if math.ceil(N / H) > 9 else '0' + str(math.ceil(N / H))
    print(Y + X)
  ```

  ```python
  # byran1302님의 풀이
  for _ in range(int(input())):
      H, W, N = map(int, input().split())
      print(str((N - 1) % H + 1) + str((N - 1) // H + 1).rjust(2,'0')) 
  ```

  * math 모듈을 활용하여 X 값을 `math.ceil(N / H)`으로 찾아주었다.

  * 다른 사람의 풀이를 보며 생각해보니 `N - 1` 로 계산후 `+1` 만 해줘도 간단히 해결할 수 있는 문제였다.

    또, `String.rjust()` method를 통해 스트링의 왼쪽에 원하는 문자를 넣는 함수도 알게되었다.

## 부녀회장이 될테야

> 난이도 : Bronze II

* [문제 링크](https://www.acmicpc.net/problem/2775)

* 입력

  첫 번째 줄에 Test case의 수 T가 주어진다. 그리고 각각의 케이스마다 입력으로 첫 번째 줄에 정수 k, 두 번째 줄에 정수 n이 주어진다. (1 <= k <= 14, 1 <= n <= 14)

* 풀이

  ```python
  for _ in range(int(input())):
    K = int(input())
    N = int(input())
    result = [i for i in range(N + 1)]
    for __ in range(K):
      for i in range(1, N + 1):
        result[i] = result[i] + result[i - 1]
    print(result[N])
  ```

  * 다른 특별한 공식이 있을 거라 생각해 많이 헤맸다.
  * 일단 제출하고 다른사람들 풀이를 보려했는데 다들 그냥 리스트 안의 값을 직접 더해주며 반복문으로 풀었었다.

## Fly me to the Alpha Centauri

> 난이도 : Silver I

* [문제 링크](https://www.acmicpc.net/problem/1011)

* 입력

  입력의 첫 줄에는 테스트케이스의 개수 T가 주어진다. 각각의 테스트 케이스에 대해 현재 위치 x 와 목표 위치 y 가 정수로 주어지며, x는 항상 y보다 작은 값을 갖는다. (0 ≤ x < y < 231)

* 풀이

  ```python
  def find(num):
    cnt = 0
    for i in range(1, num + 1):
      for j in range(2):
        cnt += 1
        num -= i
        if num <= 0:
          return cnt
  
  for _ in range(int(input())):
    X, Y = map(int, input().split())
    print(find(Y - X))
  ```

  ```python
  # pjshwa님의 풀이
  for _ in range(int(input())):
  	X, Y = map(int, input().split())
      sq = int((Y - X - 1)**0.5)
  	if Y - X > sq * sq + sq:
          print(2 * sq + 1)
  	else:
          print(2 * sq)
  ```

  * `1, 2, 3 ... , 3, 2, 1` 과 같은 방식으로 증가하는 간단한 규칙을 찾고 반복문을 돌려주었더니 `992ms`로 겨우겨우 통과했다.
  * 다른 사람들의 풀이를 보자 제곱근을 활용하여 간단하게 풀 수 있었다.