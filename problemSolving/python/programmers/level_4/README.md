# Level 4

> 고득점, 프로그래머스 랭킹을 올리기 위해!

## 목차

* [징검다리](#징검다리)
* [도둑질](#도둑질)
* [숫자 블록](#숫자-블록)
* [올바른 괄호의 갯수](#올바른-괄호의-갯수)
* [쿠키 구입](#쿠키-구입)
* [호텔 방 배정](#호텔-방-배정)
* [스티커 모으기2](#스티커-모으기2)
* [지형 편집](#지형-편집)
* [무지의 먹방 라이브](#무지의-먹방-라이브)
* [3차 자동완성](#3차-자동완성)

## 징검다리

* [문제 링크](https://programmers.co.kr/learn/courses/30/lessons/43236)

* 풀이

  ```python
  def solution(distance, rocks, n):
      right = distance
      left = 0
      while left < right:
          dist = [0] + sorted(rocks) + [distance]
          cnt = 0
          mid = (right + left + 1) // 2
          ridx, lidx = 1, 0
          while ridx < len(dist):
              if dist[ridx] - dist[lidx] < mid:
                  if ridx == len(dist) - 1:
                      before = dist[lidx]
                      cnt += 1
                      while dist[lidx] != before:
                          lidx -= 1
                  else:
                      dist[ridx] = dist[lidx]
                      ridx += 1
                      cnt += 1
              else:
                  ridx, lidx = ridx + 1, ridx
              if cnt > n:
                  break
          if cnt > n:
              right = mid - 1
          else:
              left = mid
      return left
  ```

  * 문제 카테고리가 힌트가 되어주어 쉽게 풀 수 있었던 문제였다. 이분탐색이라는 분류가 없었다면 풀이를 생각해내지 못했을 것 같다.
  * 거리의 최솟값을 기준으로 잡으면 최솟값보다 짧은 거리의 돌을 제거하며 제거한 돌이 n보다 작다면 `right`를 줄여주고 `n`보다 크거나 같다면 `left`를 높여주며 찾을 수 있다.

## 도둑질

* [문제 링크](https://programmers.co.kr/learn/courses/30/lessons/42897)

* 풀이

  ```python
  def solution(money):
      memo = [0]*(len(money) - 1)
      memo[0] = money[0]
      for i in range(1, len(money) - 1):
          if i == 1:
              memo[i] = money[i]
          elif i == 2:
              memo[i] = memo[0] + money[i]
          else:
              memo[i] = max(memo[i - 2], memo[i - 3]) + money[i]
      memo1 = [0]*(len(money))
      for i in range(1, len(money)):
          if i == 1:
              memo1[i] = money[i]
          elif i == 2:
              memo1[i] = money[i]
          else:
              memo1[i] = max(memo1[i - 2], memo1[i - 3]) + money[i]
      answer = max(memo[-1], memo[-2], memo1[-1], memo1[-2])
      return answer
  ```

  * DP로 해결할 수 있는 문제이다.
  * 인접한 두 집을 연속으로 방문하지 않아야 하므로 `i - 2`, `i - 3` 위치에서 큰 값을 메모이제이션을 통해 더해주며 저장해나가고 시작과 끝이 연결되어 있으므로 이 부분도 따로 처리해준다.

## 숫자 블록

* [문제 링크](https://programmers.co.kr/learn/courses/30/lessons/12923)

* 풀이

  ```python
  def solution(begin, end):
      answer = []
      for num in range(begin, end+1):
          if num == 1:
              answer.append(0)
          else:
              for i in range(2, int(num**0.5) + 1):
                  if not num % i and num / i <= 10000000:
                      answer.append(num/i)
                      break
              else:
                  answer.append(1)
      return answer
  ```

  * `2 ~ n^(1/2)` 까지의 숫자 중 현재 위치의 가장 작은 약수로 나누어 주면, 가장 큰 약수를 구할 수 있다.
  * 이때 가장 큰 약수가 1000,0000을 초과한다면 조건에서 벗어나므로 사용하지 않는다.

## 올바른 괄호의 갯수

* [문제 링크](https://programmers.co.kr/learn/courses/30/lessons/12929)

* 풀이

  ```python
  from math import factorial
  def parenthesisCase(n):
      return factorial(2*n)//(factorial(n)*factorial(n)*(n+1))
  ```

  ```python
  def back(left, right, strings):
      if left == n:
          result.add(strings + ')'*(n-right))
      else:
          if left > right:
              back(left, right + 1, strings + ')')
          back(left + 1, right, strings + '(')
          
  
  result = set()
  n = 0
  def solution(_):
      global n
      n = _
      back(0, 0, '')
      return len(result)
  ```

  * 카탈란 수라 불리는 수열의 대표적인 문제였다.
  * 단순하게 DFS로 완전탐색을 해주어도 풀리는지 테스트해봤는데 바로 통과가 되었다.

## 쿠키 구입

* [문제 링크](https://programmers.co.kr/learn/courses/30/lessons/49995)

* 풀이

  ```python
  def solution(cookie):
      answer = 0
      for i in range(len(cookie) - 1):
          left, leftV = i, cookie[i]
          right, rightV = i + 1, cookie[i + 1]
          while (left >= 0 or leftV > rightV) and (right <= len(cookie) - 1 or rightV > leftV):
              if leftV == rightV:
                  if answer < leftV:
                      answer = leftV
                  if left > 0:
                      left -= 1
                      leftV += cookie[left]
                  else: break
              elif leftV < rightV:
                  if left > 0:
                      left -= 1
                      leftV += cookie[left]
                  else: break
              else:
                  if right < len(cookie) - 1:
                      right += 1
                      rightV += cookie[right]
                  else: break
      return answer
  ```

  * 가운데 두 점의 위치를 찍고 왼쪽, 오른쪽 범위를 증가시키며 크기가 같을 때를 찾아주었다.

## 호텔 방 배정

* [문제 링크](https://programmers.co.kr/learn/courses/30/lessons/64063)

* 풀이

  ```python
  def solution(k, room_number):
      answer = []
      num_dict = {}
      def find(n):
          n_list = []
          while True:
              if n in num_dict:
                  n_list.append(n)
                  n = num_dict[n]
              else:
                  for nums in n_list:
                      num_dict[nums] = n + 1
                  num_dict[n] = n + 1
                  return n
      for number in room_number:
          answer.append(find(number))
      return answer
  ```

  * `num_dict`에 사용된 번호와 같은 번호가 들어왔을때 이동시켜줄 위치를 저장해주었다.
  * while문을 통해 방이 배정될때까지 반복문을 돌며 빈방을 찾아주었다.

## 스티커 모으기2

* [문제 링크](https://programmers.co.kr/learn/courses/30/lessons/12971)

* 풀이

  ```python
  def solution(sticker):
      if len(sticker) < 4:
          return max(sticker)
      memo = [0] * len(sticker)
      for i in range(len(sticker)):
          if not i:
              continue
          elif i == 1:
              memo[i] = sticker[i]
          elif i == 2:
              memo[i] = sticker[i]
              sticker[i] += sticker[0]
          elif i == len(sticker) - 1:
              memo[i] = sticker[i] + max(memo[i-2], memo[i-3])
          else:
              memo[i] = sticker[i] + max(memo[i-2], memo[i-3])
              sticker[i] += max(sticker[i-2], sticker[i-3])
      
      return max(memo[-1], memo[-2], sticker[-2], sticker[-3])
  ```

  * [도둑질](#도둑질)과 똑같은 문제였다. DP를 통해 메모이제이션을 저장하며 풀면된다.

## 지형 편집

* [문제 링크](https://programmers.co.kr/learn/courses/30/lessons/12984)

* 풀이

  ```python
  def solution(land, P, Q):
      nums = {}
      for i in range(len(land)):
          for j in range(len(land)):
              if land[i][j] not in nums:
                  nums[land[i][j]] = 1
              else:
                  nums[land[i][j]] += 1
  
      pivots = sorted(nums.keys())
      p = nums[pivots[0]]
      q = sum(nums.values()) - nums[pivots[0]]
      before = pivots[0]
      result = 0
      for key, value in sorted(nums.items()):
          result += (key - pivots[0]) * Q * value
      answer = result
      for i in range(1, len(pivots)):
          result -= (pivots[i] - before) * Q * q
          result += (pivots[i] - before) * P * p
          before = pivots[i]
          p += nums[pivots[i]]
          q -= nums[pivots[i]]
          if result < answer:
              answer = result
          
      return answer
  ```

  * 먼저 2차원 공간에서 모든 좌표의 블럭 갯수와 똑같은 갯수의 블럭이 몇개있는지를 `nums` dictionary에 저장해준다.
  * `nums.keys()` 값을 따로 리스트로 저장해 오름차순으로 정렬해 준다.
  * 정렬된 `nums.keys()` 값의 블럭 높이 정보를 받아오며 늘어난 `P` 와 줄어든 `Q` 값을 `result`에 계속해서 반영해주며 가장 적을 때를 찾으면 시간복잡도 `O(n)`으로 해결할 수 있다.

## 무지의 먹방 라이브

* [문제 링크](https://programmers.co.kr/learn/courses/30/lessons/42891)

* 풀이

  ```python
  def solution(food_times, k):
      answer = 0
      left = 0
      right = max(food_times)
      while left < right - 1:
          numsum = 0
          center = (left + right) // 2
          for time in food_times:
              if time < center:
                  numsum += time
              else:
                  numsum += center
          if numsum == k:
              left = center
              break
          elif numsum < k:
              left = center
          else:
              right = center
      for i in range(len(food_times)):
          if food_times[i] > left:
              food_times[i] -= left
              k -= left
          else:
              k -= food_times[i]
              food_times[i] = 0
      for i in range(len(food_times)):
          if food_times[i]:
              if k == 0:
                  answer = i + 1
                  break
              else:
                  k -= 1
      else:
          answer = -1
      return answer
  ```

  * 먼저 k만큼의 음식을 섭취했을 때 몇 바퀴 돌게 되는지 이분탐색을 통해 찾아주었다.
  * 찾은 값을 토대로 `k`초 후에 먹을 음식의 index위치를 찾아준다.

## 3차 자동완성

* [문제 링크](https://programmers.co.kr/learn/courses/30/lessons/17685)

* 풀이

  ```python
  def solution(words):
      words.sort()
      idx = 0
      end = len(words)
      result = [0]*end
      while idx < end - 1:
          for i in range(result[idx], len(words[idx])):
              for j in range(idx, end):
                  if i >= len(words[j]):
                      break
                  if words[j][i] != words[idx][i]:
                      break
                  result[j] += 1
                  if j < end - 1 and result[j] > result[j+1] + 1:
                      break
              if result[idx] > result[idx+1]:
                  break
          idx += 1
      return sum(result) + 1
  ```

  * 먼저 단어 리스트를 문자순으로 정렬해준다.
  * `result` 리스트를 만들어 이전 문자와 겹치는 문자의 갯수를 카운트해주며 저장해주었다.

