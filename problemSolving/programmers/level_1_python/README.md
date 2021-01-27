# Level 1 (Python)

## 목차

* [크레인 인형뽑기 게임](#크레인-인형뽑기-게임)
* [두 개 뽑아서 더하기](#두-개-뽑아서-더하기)
* [완주하지 못한 선수](#완주하지-못한-선수)
* [K번째수](#k번째수)
* [2016년](#2016년)
* [3진법 뒤집기](#3진법-뒤집기)
* [가운데 글자 가져오기](#가운데-글자-가져오기)
* [같은 숫자는 싫어](#같은-숫자는-싫어)
* [나누어 떨어지는 숫자 배열](#나누어-떨어지는-숫자-배열)
* [두 정수 사이의 합](#두-정수-사이의-합)
* [문자열 내 마음대로 정렬하기](#문자열-내-마음대로-정렬하기)
* [문자열 내 p와 y의 개수](#문자열-내-p와-y의-개수)
* [문자열 내림차순으로 배치하기](#문자열-내림차순으로-배치하기)
* [문자열 다루기 기본](#문자열-다루기-기본)
* [서울에서 김서방 찾기](#서울에서-김서방-찾기)
* [수박수박수박수박수박수?](#수박수박수박수박수박수)

## 크레인 인형뽑기 게임

* [문제 링크](https://programmers.co.kr/learn/courses/30/lessons/64061)

* 풀이

  ```python
  def solution(board, moves):
      answer = 0
      result = []
      for idx in moves:
          for i in range(len(board)):
              if board[i][idx - 1]:
                  if result and result[-1] == board[i][idx - 1]:
                      answer += 2
                      result.pop()
                      board[i][idx - 1] = 0
                      break
                  result.append(board[i][idx - 1])
                  board[i][idx - 1] = 0
                  break
      return answer
  ```
  
  * 단순히 for문으로 문제에서 말하는대로 구현만 해주면 되는 문제였다.
  * 다른 사람의 풀이를 보며 다른 특별한 풀이법이 있을까 찾아보았지만 특별한 코드는 보이지 않았다.

## 두 개 뽑아서 더하기

* [문제 링크](https://programmers.co.kr/learn/courses/30/lessons/68644)

* 풀이

  ```python
  def solution(numbers):
      answer = set()
      for i in range(len(numbers)):
          for j in range(i + 1, len(numbers)):
              answer.add(numbers[i] + numbers[j])
      return sorted(answer)
  ```
  
  * 이중 for문을 사용해 두 숫자를 뽑는 경우의 수를 모두 돌며 `answer` Set에 없는경우 추가해주었다.
  * `sorted()`를 사용해주면 list로 변환해주므로 `list()`를 써서 바꿔주지 않아도된다.

## 완주하지 못한 선수

* [문제 링크](https://programmers.co.kr/learn/courses/30/lessons/42576)

* 풀이

  ```python
  def solution(participant, completion):
      participant.sort()
      completion.sort()
      for i in range(len(participant)):
          if i == len(participant) - 1:
              return participant[i]
          if participant[i] != completion[i]:
              return participant[i]
  ```
  
  * Sort를 통해 알파벳순으로 정렬해준 후 같은 index 위치를 비교하며 다른 이름이 나올경우 출력해주었다.
  
* 다른 사람의 풀이(김형준 , ii , 홍승현 , YoungHo Choi , 민홍 외 783 명)

  ```python
  import collections
  
  
  def solution(participant, completion):
      answer = collections.Counter(participant) - collections.Counter(completion)
      return list(answer.keys())[0]
  ```

  * collections의 `Counter` 객체를 사용하면 훨씬 간단하게 해결할 수 있다.


## K번째수

* [문제 링크](https://programmers.co.kr/learn/courses/30/lessons/42748)

* 풀이

  ```python
  def solution(array, commands):
      answer = []
      for com in commands:
          com_list = array[com[0]-1:com[1]]
          answer.append(com_list[com[2]-1])
      return answer
  ```
  
* 슬라이스를 활용하여 해결하였다.

## 2016년

* [문제 링크](https://programmers.co.kr/learn/courses/30/lessons/12901)

* 풀이

  ```python
  def solution(a, b):
      answer = ''
      day = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
      month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
      total_days = 0
      for days in range(a-1):
          total_days += month[days]
      total_days += b
      answer = day[(total_days+4)%7]
      return answer
  ```


## 3진법 뒤집기

* [문제 링크](https://programmers.co.kr/learn/courses/30/lessons/68935)

* 풀이

  ```python
  def solution(n):
      answer = 0
      result = ''
      while n:
          result = str(n % 3) + result
          n //= 3
      for i in range(len(result)):
          answer += int(result[i]) * 3**i
      return answer
  ```


## 가운데 글자 가져오기

* [문제 링크](https://programmers.co.kr/learn/courses/30/lessons/12903)

* 풀이

  ```python
  def solution(s):
      answer = ''
      if len(s) % 2:
          answer += s[len(s)//2]
      else:
          answer += s[len(s)//2 - 1] + s[len(s)//2]
      return answer
  ```


## 같은 숫자는 싫어

* [문제 링크](https://programmers.co.kr/learn/courses/30/lessons/12906)

* 풀이

  ```python
  def solution(arr):
      answer = []
      p_num = -1
      for number in arr:
          if number != p_num:
              answer.append(number)
              p_num = number
      return answer
  ```


## 나누어 떨어지는 숫자 배열

* [문제 링크](https://programmers.co.kr/learn/courses/30/lessons/12910)

* 풀이

  ```python
  def solution(arr, divisor):
      answer = []
      arr.sort()
      for number in arr:
          if not number % divisor:
              answer.append(number)
      if not answer:
          answer = [-1]
      return answer
  ```


## 두 정수 사이의 합

* [문제 링크](https://programmers.co.kr/learn/courses/30/lessons/12912)

* 풀이

  ```python
  def solution(a, b):
      answer = 0
      if a <= b:
          for number in range(a, b + 1):
              answer += number
      else:
          for number in range(b, a + 1):
              answer += number
      return answer
  ```


## 문자열 내 마음대로 정렬하기

* [문제 링크](https://programmers.co.kr/learn/courses/30/lessons/12915)

* 풀이

  ```python
  def solution(strings, n):
      return sorted(strings, key=lambda x: (x[n], x))
  ```
  
  * `sorted()` 와 `lambda` 식을 사용하면 간단히 해결할 수 있다.
  * 비교할 값이 두가지 이상이라면 위와 같이 튜플로 만들어주거나 list, string 이어붙이기 등 여러방법으로 가능하다.


## 문자열 내 p와 y의 개수

* [문제 링크](https://programmers.co.kr/learn/courses/30/lessons/12916)

* 풀이

  ```python
  def solution(s):
      return s.upper().count('P') == s.upper().count('Y')
  ```


## 문자열 내림차순으로 배치하기

* [문제 링크](https://programmers.co.kr/learn/courses/30/lessons/12917)

* 풀이

  ```python
  def solution(s):
      return ''.join(sorted(s, reverse=True))
  ```
  
* `sorted()`를 사용하면 `s`를 list로 변환 후 정렬해준다. 이때, `reverse=True` 옵션을 사용하여 역순으로 정렬해주었다.

## 문자열 다루기 기본

* [문제 링크](https://programmers.co.kr/learn/courses/30/lessons/12918)

* 풀이

  ```python
  def solution(s):
      return s.isdigit() and len(s) in (4, 6)
  ```
  
  * `string.isdigit()`를 사용하여 문자열이 숫자로만 이루어졌는지 체크할 수 있다.
  

## 서울에서 김서방 찾기

* [문제 링크](https://programmers.co.kr/learn/courses/30/lessons/12919)

* 풀이

  ```python
  def solution(seoul):
      return f"김서방은 {seoul.index('Kim')}에 있다"
  ```
  
* f-string을 이용하여 간단하게 작성할 수 있다.
  * 이때, 따옴표가 겹치지 않도록 주의하자
