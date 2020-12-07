# Codeforces Global Round 12

## 목차

* [A Avoid Trygub](a-avoid-trygub)
* [B Balls of Steel](#b-balls-of-steel)

## A Avoid Trygub

* [문제 링크](https://codeforces.com/contest/1450/problem/A)

* 입력의 문자열에는 `avoidtrygub`이 숨어있다. `avoidtrygub`을 찾을 수 없도록 문자열을 섞어주어야한다.

* 풀이

  ```python
  for _ in range(int(input())):
    N = int(input())
    word = input()
    for i in range(len(word)):
      if word[i] == 'b':
        word = 'b' + word[:i] + word[i+1:]
    print(word)
  ```

  * 단순하게 문자열에서 `b` 를 찾아 모두 문자열 가장 앞으로 옮겨주어 해결하였다.

    이렇게 하면 항상 `avoidtrygu` 까지만 완성되어 `avoidtrygub` 가 나올 수 없을 것이다.

## B Balls of Steel

* [문제 링크](https://codeforces.com/contest/1450/problem/B)

* 좌표상에 여러 쇠구슬이 있다 이때 하나의 쇠구슬을 골라 K만큼의 거리에 있는 쇠구슬을 모두 끌어당기는 자력을 주어 모든 쇠구슬이 한 곳에 모일 수 있는지 알아보는 문제였다.

* 풀이

  ```python
  def find():
      N, K = map(int, input().split())
      num = []
      for __ in range(N):
        X, Y = map(int, input().split())
        num.append((X, Y))
      for i in range(N):
        for j in range(N):
          if abs(num[i][0] - num[j][0]) + abs(num[i][1] - num[j][1]) > K:
            break
        else:
          return 1
      else:
        return -1
        
  for _ in range(int(input())):
    print(find())
  ```

  * 구슬 `list`의 크기가 100으로 매우 작았다. 따라서 브루트 포스로 풀어도 시간초과는 나오지 않을 것 같아 바로 브루트 포스로 접근하였다.