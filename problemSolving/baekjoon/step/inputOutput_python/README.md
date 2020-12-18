# 입출력과 사칙연산

> https://www.acmicpc.net/step/1
>
> 기본적인 입출력과 `+, -, *, /, //, %` 등 사칙연산을 다뤄봅니다.

## 목록

* [Hello World](#hello-world)
* [We love kriii](#we-love-kriii)
* [고양이](#고양이)
* [개](#개)
* [A+B](#a+b)
* [A-B](#a-b)
* [A*B](#a*b)
* [A/B](#a/b)
* [사칙연산](#사칙연산)
* [나머지](#나머지)
* [곱셈](#곱셈)

## Hello World

> 난이도 : Bronze V

* 문제

  Hello World!를 출력하시오

* 입력

  없음

* 풀이

  ```python
  print("Hello Wolrd!")
  ```

  * 기본적인 문자열 출력을 해보는 문제였다.
  * Python에서는 `print()`를 사용해서 출력한다.

## We love kriii

> 난이도 : Bronze V

* 문제

  ACM-ICPC 인터넷 예선, Regional, 그리고 World Finals까지 이미 2회씩 진출해버린 kriii는 미련을 버리지 못하고 왠지 모르게 올 해에도 파주 World Finals 준비 캠프에 참여했다.

  대회를 뜰 줄 모르는 지박령 kriii를 위해서 격려의 문구를 출력해주자.

* 입력

  없음

* 풀이

  ```python
  print("강한친구 대한육군\n강한친구 대한육군")
  ```

  ```python
  print('''강한친구 대한육군
  강한친구 대한육군''')
  ```

  ```python
  print("강한친구 대한육군")
  print("강한친구 대한육군")
  ```

  * 위의 세가지 방법으로 풀 수 있다.
  * 문자열에 `\n`을 입력하면 줄바꿈을 할 수 있다.
  * `'''` 을 사용해서 여러 줄로된 문자열을 사용할 수 있다.
  * 기본적으로 `print()`는 한줄씩 출력하므로 단순히 두번 연속으로 입력해주어도 풀 수 있다.

## 고양이

> 난이도 : Bronze V

* 문제

  아래 예제와 같이 고양이를 출력하시오.

  ```
  \    /\
   )  ( ')
  (  /  )
   \(__)|
  ```

* 입력

  없음

* 풀이

  ```python
  print("\    /\\\n )  ( ')\n(  /  )\n \\(__)|")
  ```

  ```python
  print("\    /\\")
  print(" )  ( ')")
  print("(  /  )")
  print(" \\(__)|")
  ```

  

  * `\`와 `'`에 주의해서 풀어야한다.

  * Python `print()` 에서 `\`(backslash) 는 "escaping"이라 불리는 특수문자이다. 

    * `\t` : tab, `\n` : newline, `\r` : carriage return

    * 다른 특수문자 앞에 사용하면 일반 문자로 바꿔준다.

      input : `\\`

      output : `\`

## 개

> 난이도 : Bronze V

* 문제

  아래 예제와 같이 개를 출력하시오.

  ```
  |\_/|
  |q p|   /}
  ( 0 )"""\
  |"^"`    |
  ||_/=\\__|
  ```

* 입력

  없음

* 풀이

  ```python
  print('|\\_/|\n|q p|   /}\n( 0 )"""\\\n|"^"`    |\n||_/=\\\\__|')
  ```

  ```python
  print('|\\_/|')
  print('|q p|   /}')
  print('( 0 )"""\\')
  print('|"^"`    |')
  print('||_/=\\\\__|')
  ```

  * 문자열을 사용할 때 전체를 작은따옴표(`'`)로 묶어준 경우 큰따옴표(`"`)는 일반문자로 출력할 수 있다. (반대로도 가능)

## A+B

> 난이도 : Bronze V

* 문제

  두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

* 입력

  첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)

  ```python
  1 2
  ```

* 풀이

  ```python
  A, B = map(int, input().split())
  print(A + B)
  ```

  ```python
  print(sum(map(int, input().split())))
  ```

  * 입력받는 방법 : `map(변수타입, input().split())`
    * `split()` 괄호안의 문자를 기준으로 나눠준다. (기본값 `' '`스페이스)
  * `+` 기호를 사용해서 더해준다.
  * 기본내장함수인 `sum`을 이용해서도 풀 수 있다.

## A-B

> 난이도 : Bronze V

* 문제

  두 정수 A와 B를 입력받은 다음, A-B를 출력하는 프로그램을 작성하시오.

* 입력

  첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)

  ```
  3 2
  ```

* 풀이

  ```python
  A, B = map(int, input().split())
  print(A - B)
  ```

  * `-` 기호를 사용해서 빼준다.

## A*B

> 난이도 : Bronze V

* 문제

  두 정수 A와 B를 입력받은 다음, A×B를 출력하는 프로그램을 작성하시오.

* 입력

  첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)

  ```
  1 2
  ```

* 풀이

  ```python
  A, B = map(int, input().split())
  print(A*B)
  ```

  * `*` 기호를 사용해서 곱해준다.

## A/B

> 난이도 : Bronze IV

* 문제

  두 정수 A와 B를 입력받은 다음, A/B를 출력하는 프로그램을 작성하시오.

* 입력

  첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)

  ```
  1 3
  ```

* 풀이

  ```python
  A, B = map(int, input().split())
  print(A/B)
  ```

  * `/` 기호를 사용해서 나눠준다.

## 사칙연산

> 난이도 : Bronze IV

* 문제

  두 자연수 A와 B가 주어진다. 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오. 

* 입력

  두 자연수 A와 B가 주어진다. (1 ≤ A, B ≤ 10,000)

  ```
  7 3
  ```

* 풀이

  ```python
  A, B = map(int, input().split())
  print(A+B)
  print(A-B)
  print(A*B)
  print(A//B)
  print(A%B)
  ```

  * `//` 으로 몫을 `%` 로 나머지를 구할 수 있다.

## 나머지

> 난이도 : Bronze V

* 문제

  (A+B)%C는 ((A%C) + (B%C))%C 와 같을까?

  (A×B)%C는 ((A%C) × (B%C))%C 와 같을까?

  세 수 A, B, C가 주어졌을 때, 위의 네 가지 값을 구하는 프로그램을 작성하시오.

* 입력

  첫째 줄에 A, B, C가 순서대로 주어진다. (2 ≤ A, B, C ≤ 10000)

  ```
  5 8 4
  ```

* 풀이

  ```python
  A, B, C = map(int, input().split())
  print((A + B) % C)
  print((A%C + B%C) % C)
  print(A * B % C)
  print((A%C) * (B%C) % C)
  ```

  * 사칙연산의 우선순위에 대해 알아보는 문제이다.

    |          Operator          |          Description           |
    | :------------------------: | :----------------------------: |
    |            `**`            |              지수              |
    |          `~ + -`           |     단항 플러스와 마이너스     |
    |         `* / % //`         |   곱하기, 나누기, 나머지, 몫   |
    |           `+ -`            |          덧셈과 뺄셈           |
    |          `>> <<`           |        좌우 비트 시프트        |
    |            `&`             |           비트 'AND'           |
    |           `^ |`            | 비트 전용 'OR'와 정기적인 'OR' |
    |        `<= < > >=`         |          비교 연산자           |
    |         `<> == !=`         |          평등 연산자           |
    | `= %= /= //= -= += *= **=` |          할당 연산자           |
    |        `is is not`         |          식별 연산자           |
    |        `in not in`         |          맴버 연산자           |
    |        `not or and`        |          논리 연산자           |

## 곱셈

> 난이도 : Bronze IV

* 문제

  (세 자리 수) × (세 자리 수)는 다음과 같은 과정을 통하여 이루어진다.

  ![img](https://www.acmicpc.net/upload/images/f5NhGHVLM4Ix74DtJrwfC97KepPl27s%20(1).png)

  (1)과 (2)위치에 들어갈 세 자리 자연수가 주어질 때 (3), (4), (5), (6)위치에 들어갈 값을 구하는 프로그램을 작성하시오.

* 입력

  첫째 줄에 (1)의 위치에 들어갈 세 자리 자연수가, 둘째 줄에 (2)의 위치에 들어갈 세자리 자연수가 주어진다.

  ```
  472
  385
  ```

* 풀이

  ```python
  A = int(input())
  B = input()
  results = [A * int(B[i]) for i in range(len(B) - 1, -1, -1)] + [A * int(B)]
  for result in results:
    print(result)
  ```

  * 입력을 그냥 받으면 문자열로 받아진다.
  * 입력받은 문자열을 1의 자리부터 하나씩 integer로 바꿔주며 A와 곱해주었다.

