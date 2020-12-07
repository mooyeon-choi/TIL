# if문

> Python에서 if문의 사용법을 알아보자

## 목록

* [두 수 비교하기](#두-수-비교하기)
* [시험 성적](#시험-성적)
* [윤년](#윤년)
* [사분면 고르기](#사분면-고르기)
* [알람 시계](#알람-시계)

## 두 수 비교하기

> 난이도 : Bronze IV

* 문제

  두 정수 A와 B가 주어졌을 때, A와 B를 비교하는 프로그램을 작성하시오.

* 입력

  첫째 줄에 A와 B가 주어진다. A와 B는 공백 한 칸으로 구분되어져 있다.

* 풀이

  ```python
  A, B = map(int, input().split())
  print('>' if A > B else '<' if A < B else '==')
  ```

  ```python
  A, B = map(int, input().split())
  if A > B:
      print('>')
  elif A < B:
      print('<')
  else:
      print('==')
  ```

  * `if, elif, else` 의 활용법을 묻는 문제다.
  * `result = '>' if A > B else '<'` 와 같은 방법으로 한줄로 쓸 수도 있다.

## 시험 성적

> 난이도 : Bronze IV

* 문제

  시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.

* 입력

  첫째 줄에 시험 점수가 주어진다. 시험 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.

* 풀이

  ```python
  score = int(input())
  print('A' if score >= 90 else 'B' if score >= 80 else 'C' if score >= 70 else 'D' if score >= 60 else 'F')
  ```

  ```python
  score = int(input())
  if score >= 90:
      print('A')
  elif score >= 80:
      print('B')
  elif score >= 70:
      print('C')
  elif score >= 60:
      print('D')
  else:
      print('F')
  ```

  * 이전 조건에 포함되지 않는 경우 다음 `elif`로 넘어가므로  

    ```python
    elif 90 > score >= 80:
        print('B')
    ```

    와 같이 처리해줄 필요가 없다.

## 윤년

> 난이도 : Bronze IV

* 문제

  연도가 주어졌을 때, 윤년이면 1, 아니면 0을 출력하는 프로그램을 작성하시오.

  윤년은 연도가 4의 배수이면서, 100의 배수가 아닐 때 또는 400의 배수일 때이다.

  예를 들어, 2012년은 4의 배수이면서 100의 배수가 아니라서 윤년이다. 1900년은 100의 배수이고 400의 배수는 아니기 때문에 윤년이 아니다. 하지만, 2000년은 400의 배수이기 때문에 윤년이다.

* 입력

  첫째 줄에 연도가 주어진다. 연도는 1보다 크거나 같고, 4000보다 작거나 같은 자연수이다.

* 풀이

  ```python
  year = int(input())
  print(1 if not year % 400 else 0 if not year % 100 else 1 if not year % 4 else 0)
  ```

  ```python
  year = int(input())
  if year % 400 == 0:
      print(1)
  elif year % 100 == 0:
      print(0)
  elif year % 4 == 0:
      print(1)
  else:
      print(0)
  ```

  * 위 시험 성적 문제와 같은 방식으로 풀면된다.
  * integer 0 은 boolean false로 표시되고 다른 값은 true로 표시되므로 이를 활용해 `if not year % 400` 으로도 써줄 수 있다.

## 사분면 고르기

> 난이도 : Bronze IV

* 문제

  흔한 수학 문제 중 하나는 주어진 점이 어느 사분면에 속하는지 알아내는 것이다. 사분면은 아래 그림처럼 1부터 4까지 번호를 갖는다. "Quadrant n"은 "제n사분면"이라는 뜻이다.

  ![img](https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/14681/1.png)

  예를 들어, 좌표가 (12, 5)인 점 A는 x좌표와 y좌표가 모두 양수이므로 제1사분면에 속한다. 점 B는 x좌표가 음수이고 y좌표가 양수이므로 제2사분면에 속한다.

  점의 좌표를 입력받아 그 점이 어느 사분면에 속하는지 알아내는 프로그램을 작성하시오. 단, x좌표와 y좌표는 모두 양수나 음수라고 가정한다.

* 입력

  첫 줄에는 정수 x가 주어진다. (−1000 ≤ x ≤ 1000; x ≠ 0) 다음 줄에는 정수 y가 주어진다. (−1000 ≤ y ≤ 1000; y ≠ 0)

* 풀이

  ```python
  location = [int(input()) for _ in range(2)]
  print((1 if location[0] > 0 else 2) if location[1] > 0 else (4 if location[0] > 0 else 3))
  ```

  ```python
  x, y = map(int, input().split())
  if x > 0:
      if y > 0:
          print(1)
      else:
          print(4)
  else:
      if y > 0:
          print(2)
      else:
          print(3)
  ```

  * `if` 와 `else`를 활용하면 풀 수 있는 문제였다.

## 알람 시계

> 난이도 : Bronze III

* 문제

  상근이는 매일 아침 알람을 듣고 일어난다. 알람을 듣고 바로 일어나면 다행이겠지만, 항상 조금만 더 자려는 마음 때문에 매일 학교를 지각하고 있다.

  상근이는 모든 방법을 동원해보았지만, 조금만 더 자려는 마음은 그 어떤 것도 없앨 수가 없었다.

  이런 상근이를 불쌍하게 보던, 창영이는 자신이 사용하는 방법을 추천해 주었다.

  바로 "45분 일찍 알람 설정하기"이다.

  이 방법은 단순하다. 원래 설정되어 있는 알람을 45분 앞서는 시간으로 바꾸는 것이다. 어차피 알람 소리를 들으면, 알람을 끄고 조금 더 잘 것이기 때문이다. 이 방법을 사용하면, 매일 아침 더 잤다는 기분을 느낄 수 있고, 학교도 지각하지 않게 된다.

  현재 상근이가 설정한 알람 시각이 주어졌을 때, 창영이의 방법을 사용한다면, 이를 언제로 고쳐야 하는지 구하는 프로그램을 작성하시오.

* 입력

  첫째 줄에 두 정수 H와 M이 주어진다. (0 ≤ H ≤ 23, 0 ≤ M ≤ 59) 그리고 이것은 현재 상근이가 설정한 놓은 알람 시간 H시 M분을 의미한다.

  입력 시간은 24시간 표현을 사용한다. 24시간 표현에서 하루의 시작은 0:0(자정)이고, 끝은 23:59(다음날 자정 1분 전)이다. 시간을 나타낼 때, 불필요한 0은 사용하지 않는다.

* 풀이

  ```python
  H, M = map(int, input().split())
  
  if M < 45:
    if H: 
      H -= 1
    else:
      H += 23 
    M += 15
  else:
    M -= 45
    
  print(H, M)
  ```

  * `H, M` 의 값을 `if else`로 나누어 처리해주면 되는 문제였다.
  * 한줄 코딩으로 할 경우 너무 복잡해져 가독성이 떨어지므로 한줄 코딩으로는 풀지 않았다.