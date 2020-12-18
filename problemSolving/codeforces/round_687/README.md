# [Codeforces Round 687 (Div. 2)](https://codeforces.com/blog/entry/85081)

> 두 번째로 참가한 Codeforces contest였다.
>
> python3으로 코드를 제출해서 통과하지 못한 문제를 pypy3으로 제출하니 바로 통과가 되었다..
>
> python 참가자들은 pypy3으로 제출하도록 하자

## 목차

* [A_Prison Break](#prison-break)
* [B_Repainting Street](#repainting-street)

## Prison Break

* [문제 링크](https://codeforces.com/contest/1457/problem/A)

* 행렬의 크기가 주어지고 모든 위치에서 하나의 공간으로 이동한다.

* 이때 가장 오래걸리는 경우는 네 꼭지점 위치에서 지정된 좌표까지의 이동 거리이므로 이를 통해 해결하였다.

* 풀이

  ```python
  T = int(input())
  for _ in range(T):
    N, M, R, C = map(int, input().split())
    print(max(N - R, R - 1) + max(M - C, C - 1))
  ```

## Repainting Street

> python3로는 18번 테스트케이스에서 시간초과가 났고 pypy3으로는 통과하였다. 제출이력을 보니 python3으로도 통과할 수 있는 방법이 있는 것 같지만, 앞으로 pypy3을 쓰는게 좋을 것 같다.

* [문제 링크](https://codeforces.com/contest/1457/problem/B)

* `K` 범위 만큼의 값을 바꿔주며 모두 하나의 숫자가 될 수 있을때까지 반복한다.

* 해시로 각 숫자별 카운팅 메모리를 만들어주고 `key` 값의 숫자와 현재 index의 숫자가 다를경우 카운트를 증가시키며 풀어주었다.

  이때, `K` 범위 내에서 같은 숫자가 중간에 하나씩 끼어있는 경우 이를 포함하도록 해야하므로 카운트를 항상 최대 범위인 `K`만큼씩 세주도록 하였다.

* 풀이

  ```python
  T = int(input())
  for _ in range(T):
    N, K = map(int, input().split())
    resultDict = {}
    cntDict = {}
    C = list(map(int, input().split()))
    for num in set(C):
      resultDict[num] = 0
      cntDict[num] = 0
    for num in C:
      for key in resultDict.keys():
        if key != num:
          cntDict[key] += 1
          if cntDict[key] >= K:
            resultDict[key] += 1
            cntDict[key] = 0
        else:
          if cntDict[key]:
            cntDict[key] += 1
            if cntDict[key] >= K:
              resultDict[key] += 1
              cntDict[key] = 0
    for key in cntDict.keys():
      if cntDict[key]:
        resultDict[key] += 1
    print(min(resultDict.values()))
  ```

