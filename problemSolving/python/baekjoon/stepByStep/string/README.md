# 문자열

> Python의 장점! 하면 항상 들어가는 것 중 하나가 문자열 처리가 쉽다이다. Python에서 문자열의 처리를 배워보자

## 목차

* [아스키 코드](#아스키-코드)
* [숫자의 합](#숫자의-합)
* [알파벳 찾기](#알파벳-찾기)
* [문자열 반복](#문자열-반복)
* [단어 공부](#단어-공부)
* [단어의 개수](#단어의-개수)
* [상수](#상수)
* [다이얼](#다이얼)
* [크로아티아 알파벳](#크로아티아-알파벳)
* [그룹 단어 체커](#그룹-단어-체커)

## 아스키 코드

> 난이도 Bronze V

* 문제

  알파벳 소문자, 대문자, 숫자 0-9중 하나가 주어졌을 때, 주어진 글자의 아스키 코드값을 출력하는 프로그램을 작성하시오.

* 입력

  알파벳 소문자, 대문자, 숫자 0-9 중 하나가 첫째 줄에 주어진다.

* 풀이

  ```python
  print(ord(input()))
  ```

  * `ord()`를 사용하면 해당 문자를 아스키 코드로 변환해준다.

## 숫자의 합

> 난이도 Bronze II

* 문제

  N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.

* 입력

  첫째 줄에 숫자의 개수 N (1 ≤ N ≤ 100)이 주어진다. 둘째 줄에 숫자 N개가 공백없이 주어진다.

* 풀이

  ```python
  N = input()
  print(sum(map(lambda x: int(x), input())))
  ```

  ```python
  N = input()
  answer = 0
  for num in input():
      answer += int(num)
  print(answer)
  ```

  * 두가지 방법으로 풀어보았다.

  * 아래는 기본적인 풀이법으로 Python for문은 기본적으로 for each로 동작하는데 이를 활용해서 String의 각 인덱스에 위치한 숫자를 가져와 Integer로 변환해준 후 더해주었다.

  * 위는 Python의 `map()` 과 `lambda` 를 활용해서 간단하게 짜보았다.

    input()의 각 인덱스 숫자(String)가 Integer로 변환되어 map에 저장된다. 이를 마지막에 `sum()`을 사용해 모두 더한 값을 구해주었다.

## 알파벳 찾기

> 난이도 : Bronze II

* 문제

  알파벳 소문자로만 이루어진 단어 S가 주어진다. 각각의 알파벳에 대해서, 단어에 포함되어 있는 경우에는 처음 등장하는 위치를, 포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.

* 입력

  첫째 줄에 단어 S가 주어진다. 단어의 길이는 100을 넘지 않으며, 알파벳 소문자로만 이루어져 있다.

* 풀이

  * 먼저 `a`, `z`의 아스키 코드를 알아보자.

    ```python
    print(ord('a')) #=> 97
    print(ord('z')) #=> 122
    ```

  * 위의 값을 통해 우리는 길이가 26인 List가 필요하고 index가 0부터 시작하기 위해서는 각 아스키 코드에 `-97`을 해줘야 한다는 것을 알 수 있다.

  * 이를 통해 문제를 풀어보면

    ```python
    result = ['-1'] * 26
    word = input()
    for i in range(len(word)):
      if result[ord(word[i]) - 97] == '-1':
        result[ord(word[i]) - 97] = str(i)
    print(' '.join(result))
    ```

    와 같이 해결할 수 있다.

  * `.join`을 사용하기 위해 숫자를 String으로 변환후 List에 추가해주었다.

## 문자열 반복

> 난이도 : Bronze II

* 문제

  문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오. 즉, 첫 번째 문자를 R번 반복하고, 두 번째 문자를 R번 반복하는 식으로 P를 만들면 된다. S에는 QR Code "alphanumeric" 문자만 들어있다.

  QR Code "alphanumeric" 문자는 `0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./:` 이다.

* 입력

  첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)가 주어진다. 각 테스트 케이스는 반복 횟수 R(1 ≤ R ≤ 8), 문자열 S가 공백으로 구분되어 주어진다. S의 길이는 적어도 1이며, 20글자를 넘지 않는다. 

* 풀이

  ```python
  T = int(input())
  for _ in range(T):
    N, word = map(str, input().split())
    result = ''
    for string in word:
      result += string * int(N)
    print(result)
  ```

  * `String` + `String` 로 두 문자열을 이어줄 수 있다.
  * `String` * `Integer` 로 문자열을 `Integer` 횟수만큼 반복해서 이어줄 수 있다.

## 단어 공부

> 난이도 : Bronze I

* 문제

  알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.

* 입력

  첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.

* 풀이

  ```python
  word = input().upper()
  alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  maxStr, maxCnt = '?', 0
  for alpha in alphabet:
    cnt = word.count(alpha)
    if cnt > maxCnt:
      maxStr, maxCnt = alpha, cnt
    elif cnt == maxCnt:
      maxStr = '?'
  print(maxStr)
  ```

  * `String.upper()` 로 모든 알파벳을 대문자로 바꿀 수 있다.
  * `String.count()`로 특정 문자의 갯수를 셀 수 있다.

## 단어의 개수

> 난이도 : Bronze II

* 문제

  영어 대소문자와 띄어쓰기만으로 이루어진 문자열이 주어진다. 이 문자열에는 몇 개의 단어가 있을까? 이를 구하는 프로그램을 작성하시오. 단, 한 단어가 여러 번 등장하면 등장한 횟수만큼 모두 세어야 한다.

* 입력

  첫 줄에 영어 대소문자와 띄어쓰기로 이루어진 문자열이 주어진다. 이 문자열의 길이는 1,000,000을 넘지 않는다. 단어는 띄어쓰기 한 개로 구분되며, 공백이 연속해서 나오는 경우는 없다. 또한 문자열의 앞과 뒤에는 공백이 있을 수도 있다.

* 풀이

  ```python
  print(len(input().split()))
  ```

  * 파이썬에서 문자열 처리가 쉽다고 하는 가장 큰 이유 중 하나이다.
  * 문자열을 나눠주려면 간단히 `String.split()` 을 이용하면 된다. (Default: ' ')

## 상수

> 난이도 : Bronze II

* 문제

  상근이의 동생 상수는 수학을 정말 못한다. 상수는 숫자를 읽는데 문제가 있다. 이렇게 수학을 못하는 상수를 위해서 상근이는 수의 크기를 비교하는 문제를 내주었다. 상근이는 세 자리 수 두 개를 칠판에 써주었다. 그 다음에 크기가 큰 수를 말해보라고 했다.

  상수는 수를 다른 사람과 다르게 거꾸로 읽는다. 예를 들어, 734와 893을 칠판에 적었다면, 상수는 이 수를 437과 398로 읽는다. 따라서, 상수는 두 수중 큰 수인 437을 큰 수라고 말할 것이다.

  두 수가 주어졌을 때, 상수의 대답을 출력하는 프로그램을 작성하시오.

* 입력

  첫째 줄에 상근이가 칠판에 적은 두 수 A와 B가 주어진다. 두 수는 같지 않은 세 자리 수이며, 0이 포함되어 있지 않다.

* 풀이

  ```python
  print(max(map(lambda x: x[::-1], input().split())))
  ```

  ```python
  N, M = input().split()
  print(max(N[::-1], M[::-1]))
  ```

  * 두 수의 길이가 같아서 쓸 수 있는 방법이다.
  * 파이썬에서 문자끼리 크기를 비교해주면 아스키 코드를 기준으로 비교해준다. 이때 비교는 index를 기준으로 이루어진다. 따라서 두 문자열의 길이가 다를 경우 사용할 수 없는 방법이다.

## 다이얼

> 난이도 : Bronze II

* [문제 링크](https://www.acmicpc.net/problem/5622)

* 입력

  첫째 줄에 알파벳 대문자로 이루어진 단어가 주어진다. 단어는 2글자~15글자로 이루어져 있다.

* 풀이

  ```python
  change = {
    'A': 3, 'B': 3, 'C': 3,
    'D': 4, 'E': 4, 'F': 4,
    'G': 5, 'H': 5, 'I': 5,
    'J': 6, 'K': 6, 'L': 6,
    'M': 7, 'N': 7, 'O': 7,
    'P': 8, 'Q': 8, 'R': 8, 'S': 8,
    'T': 9, 'U': 9, 'V': 9,
    'W': 10, 'X': 10, 'Y': 10, 'Z': 10
  }
  answer = 0
  for string in input():
    answer += change[string]
  print(answer)
  ```

  * 가끔은 무식해보이는 방법이 가장 좋다...

## 크로아티아 알파벳

> 난이도 : Silver V

* [문제 링크](https://www.acmicpc.net/problem/2941)

* 입력

  첫째 줄에 최대 100글자의 단어가 주어진다. 알파벳 소문자와 '-', '='로만 이루어져 있다.

  단어는 크로아티아 알파벳으로 이루어져 있다. 문제 설명의 표에 나와있는 알파벳은 변경된 형태로 입력된다.

* 풀이

  ```python
  word = input()
  for repls in ('c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z='):
    word = word.replace(repls, 'C', 100)
  print(len(word))
  ```

  ```python
  # 다른 사람들이 푼 방식
  word = input()
  print(len(word) - sum(map(word.count, ('=', '-', 'dz=', 'lj', 'nj'))))
  ```

  * `dz=` 와 `z=` 중복으로 카운트 될 수 있다고 생각해 replace를 통해 모두 `C`로 바꿔주었다.

  * 다른 사람들은 어떻게 풀었나 확인했더니 아래와 같은 방식으로 푼 사람들이 많았다.

    `dz=`는 `=`로 한번더 카운트돼서 안될 것 같은데 돌려보니 제대로 통과했다.

    나도 정확하게 이해는 못하겠다....

## 그룹 단어 체커

> 난이도 : Silver V

* 문제

  그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다. 예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만, aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.

  단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.

* 첫째 줄에 단어의 개수 N이 들어온다. N은 100보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에 단어가 들어온다. 단어는 알파벳 소문자로만 되어있고 중복되지 않으며, 길이는 최대 100이다.

* 풀이

  ```python
  answer = 0
  for _ in range(int(input())):
    word = input()
    before, used = '', set()
    for string in word:
      if not before:
        before = string
        continue
      if before != string:
        used.add(before)
        before = string
        if string in used:
          break
    else:
      answer += 1
  print(answer)
  ```

  ```python
  # baek4055 님의 풀이
  answer = 0
  for i in range(int(input())):
      word = input()
      if list(word) == sorted(word, key=word.find):
          answer += 1
  print(answer)
  ```

  * 연속하지 않는 문자가 나왔을 때, 이전에 사용된적이 있는지 확인하며 찾아주었다.

  * 다른 사람들은 어떻게 풀었나 둘러봤는데 [baek4055](https://www.acmicpc.net/user/baek4055) 님의 풀이가 너무 신기해서 가져왔다.

    알파벳이 처음 찍힌 index를 기준으로 Sort를 진행해주어 연속하지 않는 같은 문자가 발생하였을때, 기존의 입력과 달라지는 것을 이용하여 체크하였다.

    Sort의 새로운 활용법을 알게된 좋은 문제였다.

