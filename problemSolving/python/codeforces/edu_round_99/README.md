# Educational Codeforces Round 99 (Rated for Div. 2)

> 문제가 수능 영어지문 수준으로 이해하기 힘들게 써있어서 많이 해맸다. 3줄만에 끝날 문제를 냈을리가 없다고 생각하고 또, 제출 했다가 틀리면 감점이 당하니까 혼자 열심히 생각해보다가 그냥 제출했더니 통과했다...

## 목차

* [A_Strange Functions](#a_strange-functions)
* [C_Ping-pong](#c_ping-pong)

## A_Strange Functions

* [문제링크](https://codeforces.com/contest/1455/problem/A)

* 결국 `1, 10, 100, 1000, ...` 만 나오므로 input의 String length를 구하면 되는 문제였다.

* 풀이

  ```python
  T = int(input())
  for _ in range(T):
    print(len(input()))
  ```

## C_Ping-pong

* [문제링크](https://codeforces.com/contest/1455/problem/C)

* Alice는 항상 먼저 시작해야하기 때문에 선택지가 없다.

* Bob은 Alice의 마지막 서브공만 받아쳤을 때 가장 큰점수를 Alice의 점수를 깎으면서 얻을 수 있다.

* 따라서, `Alice의 stamina - 1, Bob의 stamina` 가 정답으로 나온다.

* 풀이

  ```python
  T = int(input())
  for _ in range(T):
    X, Y = map(int, input().split())
    print(X - 1, Y)
  ```

  