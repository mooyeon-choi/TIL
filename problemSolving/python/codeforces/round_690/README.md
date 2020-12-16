# Codeforces Round #690 (Div. 3)

> 2020년 12월 15일 23:35에 열린 Contest
>
> 시간만 더 주어진다면 문제를 다 풀 수 있었을 것 같다. 효율성을 고려한 풀이방법이 바로 생각나지 않아 코드를 제출하며 수정한게 많았다. 처음부터 생각할 수 있도록 더 연습하자!

## 목차

* [A Favorite Sequence](#a-favorite-sequence)
* [B Last Years Substring](#b-last-years-substring)
* [C Unique Number](#c-unique-number)
* [D Add to Neighbour and Remove](#d-add-to-neighbour-and-remove)
* [E1 Close Tuples easy version](#e1-close-tuples-easy-version)

## A Favorite Sequence

* [문제 링크](https://codeforces.com/contest/1462/problem/A)

* 입력받은 리스트의 왼쪽, 오른쪽 요소들을 끝에서 부터 하나씩 번갈아가며 출력하는 문제였다.

* 풀이

  ```python
  for _ in range(int(input())):
    N = int(input())
    nums = input().split()
    left, right = 0, N - 1
    result = []
    if left == right:
        result.append(nums[left])
    while left < right:
      result.append(nums[left])
      result.append(nums[right])
      left += 1
      right -= 1
      if left == right:
        result.append(nums[left])
    print(' '.join(result))
  ```

  * 더 간단한 풀이도 많겠지만 List의 크기가 작아 시간초과는 나지 않을 것 같아 확실한 방법으로 `result` List를 만들어주고 양쪽에서 하나씩 넣어주어 새로운 List를 만들어주었다.

## B Last Years Substring

* [문제 링크](https://codeforces.com/contest/1462/problem/B)

* 입력받은 문자열의 가운데 구간을 한번 잘라내 '2020'을 만들 수 있는지 묻는 문제였다.

* 풀이

  ```python
  for _ in range(int(input())):
    n = int(input())
    word = input()
    if '2020' == word[-4:]:
      print('YES')
    elif '2' == word[0] and '020' == word[-3:]:
      print('YES')
    elif '20' == word[:2] and '20' == word[-2:]:
      print('YES')
    elif '202' == word[:3] and '0' == word[-1]:
      print('YES')
    elif '2020' == word[:4]:
      print('YES')
    else:
      print('NO')
  ```

  * 경우의 수가 적어 단순히 if문으로 만들어 줄 수 있고 효율성으로도 가장 좋을 것 같아 하나하나 if문으로 만들어 주었다.

## C Unique Number

* [문제 링크](https://codeforces.com/contest/1462/problem/C)

* `0 ~ 9`의 숫자를 하나씩 이어붙여 모든 자리 숫자의 합이 주어진 `n`이 되는 경우를 이때 이어붙인 숫자의 크기가 가장 작은 것을 출력하는 문제였다.

* 풀이

  ```python
  def find(num, idx):
    if sum(num) == n:
      result.append(''.join(map(str,num)))
    elif sum(num) > n or idx > 9:
      return
    for i in range(idx, 10):
      find(num + [i], i + 1)
  
  for _ in range(int(input())):
    n = int(input())
    result = []
    find([], 0)
    print(min(map(int, result)) if result else -1)
  ```

  * List의 총 크기가 10으로 재귀로 풀어도 재귀횟수초과나 시간초과가 날 일은 없을 것이라 생각해 재귀로 풀어주었다.
  * 가장 작은 수를 찾는 문제이므로 합이 n이 되는 숫자의 조합에서 작은 수가 앞에 오는 경우만 보면 된다.
  * `0`이 가장 앞에 올 경우 없는 거나 마찬가지이므로 `1 ~ 9` 까지만 해주어도 된다.
  * `1 ~ 9` 까지의 숫자 중 `m`개의 조합으로 합이 `n`이 되는 경우를 찾고 그 중 가장 작은 값을 출력해주었다.

## D Add to Neighbour and Remove

* [문제 링크](https://codeforces.com/contest/1462/problem/D)

* 서로 인접한 값들을 더 해주며 List안의 값이 모두 같은 숫자가 되도록 만들어줄때 가장 적은 횟수로 만들 수 있는 방법을 찾는 문제였다.

* 풀이

  ```python
  for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    idx = 1
    check = False
    while not check:
      if idx == n:
        cnt = idx - 1
        check = True
      num = sum(nums[:idx])
      numsum = 0
      cnt = idx - 1
      for i in range(idx, n):
        numsum += nums[i]
        if numsum == num:
          numsum = 0
        elif numsum > num:
          break
        else:
          cnt += 1
      else:
        if not numsum:
          check = True
      idx += 1
    print(cnt)
  ```

  * List `nums`의 `0 ~ idx` 까지 값의 합을 기준으로 반복문을 돌며 뒤에서도 같은 크기의 값을 만들어 줄 수 있는지 확인하고 만들어지지 않는다면 `idx`를 `1`씩 증가시키며 다시 체크해주었다.

## E1 Close Tuples easy version

* [문제 링크](https://codeforces.com/contest/1462/problem/E1)

* 입력받은 List에서 3개의 요소를 고르고 그 중 `가장 큰 값 - 가장 작은 값`의 크기가 2이하인 경우의수 를 찾는 문제였다.

* 풀이

  ```python
  import sys
  
  for _ in range(int(input())):
    n = int(sys.stdin.readline())
    nums = list(map(int, sys.stdin.readline().split()))
    nums.sort()
    answer = 0
    idx = 0
    before = 0
    for i in range(n - 2):
      if nums[i] == before:
        if idx - i >= 2:
          answer += (idx - i) * (idx - i - 1) // 2
        continue
      else:
        before = nums[i]
        idx = i
      for j in range(i+1, n):
        if nums[j] - nums[i] > 2:
          idx = j - 1
          break
      else:
        idx = j
      if idx - i >= 2:
        answer += (idx - i) * (idx - i - 1) // 2
    print(answer)
  ```

  * 입력받은 List를 작은 값부터 정렬해주고 기준점 `i`에서 `nums[i] + 2`보다 작거나 같은 수의 마지막 index를 찾고

    <sub>index - i</sub>C<sub>2</sub> 를 계산해주어 answer에 더해주었다. 

