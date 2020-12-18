# [Codeforces Round #688 (Div. 2)](https://codeforces.com/contest/1453)

> 어리굴젓을 먹었다가 노로 바이러스로 인한 식중독 때문에 참여하지 못할뻔 했다. 그래도 한문제만 풀어서 감점은 당하지 말자는 생각으로 스마트폰으로 참여했는데 두문제를 풀어 점수도 생각보다 많이 올랐다!
>
> 디버깅을 해볼 수 없고 코드를 보기도 불편해 자잘한 에러가 많이났고 감점도 많이 당했지만 만족스러운 결과였다.

## 목차

* [A Cancel the Trains](#a-cancel-the-trains)
* [B Suffix Operations](#b-suffix-operations)

## A Cancel the Trains

* [문제 링크](https://codeforces.com/contest/1453/problem/A)

* 두 줄에 걸쳐 왼쪽에서 출발하는 열차, 아래에서 출발하는 열차의 플렛폼 번호가 입력으로 들어온다.

* 이 때 겹치는 플렛폼 번호의 갯수를 구하면 되는 문제였다.

* 풀이

  ```python
  for _ in range(int(input())):
    N, M = map(int, input().split())
    N_list = set(input().split())
    M_list = set(input().split())
    print(len(N_list & M_list))
  ```

  * 간단하게 Set을 활용하여 교집합의 크기를 출력해주었다.

## B Suffix Operations

* [문제 링크](https://codeforces.com/contest/1453/problem/B)

* 항상 `i < j <= n` 인덱스의 값들을 동일하게 변경하며 진행한다.

* 따라서, 직전 인덱스의 숫자와 얼마나 차이가 나는지만 보면 총 값을 몇번 변경해주었는지 구할 수 있다.

* 또 한단계 건너뛰었을 경우와 그냥 진행했을때의 차이를 구하고 그 값의 차이가 가장 큰경우를 제외하면 값을 최소로 변경해주기 위해 바꿔야할 숫자 인덱스의 위치를 구할 수 있다.

* 풀이

  ```python
  for _ in range(int(input())):
    N = int(input())
    num = list(map(int, input().split()))
    result = 0
    maxNum = max(abs(num[-1] - num[-2]), abs(num[0] - num[1]))
    for i in range(1, N -1):
      result += abs(num[i] - num[i-1])
      if maxNum < abs(num[i] - num[i-1]) + abs(num[i+1] - num[i]) - abs(num[i+1] - num[i-1]):
          maxNum = abs(num[i] - num[i-1]) + abs(num[i+1] - num[i]) - abs(num[i+1] - num[i-1])
    result += abs(num[-1] - num[-2])
    print(result - maxNum)
  ```

  