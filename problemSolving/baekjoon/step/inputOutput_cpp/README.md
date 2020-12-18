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

  ```cpp
  #include <iostream>
  using namespace std;
  int main()
  {
    cout << "Hello World!";
  }
  ```


## We love kriii

> 난이도 : Bronze V

* 문제

  ACM-ICPC 인터넷 예선, Regional, 그리고 World Finals까지 이미 2회씩 진출해버린 kriii는 미련을 버리지 못하고 왠지 모르게 올 해에도 파주 World Finals 준비 캠프에 참여했다.

  대회를 뜰 줄 모르는 지박령 kriii를 위해서 격려의 문구를 출력해주자.

* 입력

  없음

* 풀이

  ```cpp
  #include <iostream>
  using namespace std;
  int main()
  {
    cout << "강한친구 대한육군\n강한친구 대한육군";
  }
  ```


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

  ```cpp
  #include <iostream>
  using namespace std;
  int main() {
  	cout << "\\    /\\\n )  ( ')\n(  /  )\n \\(__)|";
  }
  ```


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

  ```cpp
  #include <iostream>
  using namespace std;
  int main() {
  	cout << "|\\_/|\n|q p|   /}\n( 0 )\"\"\"\\\n|\"^\"`    |\n||_/=\\\\__|";
  }
  ```


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

  ```cpp
  #include <iostream>
  using namespace std;
  int A, B;
  int main() {
  	cin >> A >> B;
  	cout << A + B;
  }
  ```


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

  ```cpp
  #include <iostream>
  using namespace std;
  int A, B;
  int main() {
  	cin >> A >> B;
  	cout << A - B;
  }
  ```


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

  ```cpp
  #include <iostream>
  using namespace std;
  int A, B;
  int main() {
  	cin >> A >> B;
  	cout << A * B;
  }
  ```


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

  ```cpp
  #include <iostream>
  using namespace std;
  double A, B;
  int main()
  {
    cin >> A >> B;
    cout.precision(10);
    cout << A / B;
  }
  ```


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

  ```cpp
  #include <iostream>
  using namespace std;
  int A, B;
  int main()
  {
    cin >> A >> B;
    cout << A + B << '\n'
         << A - B << '\n'
         << A * B << '\n'
         << A / B << '\n'
         << A % B;
  }
  ```


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

  ```cpp
  #include <iostream>
  using namespace std;
  int A, B, C;
  int main()
  {
    cin >> A >> B >> C;
    cout << (A + B) % C << '\n'
         << (A % C + B % C) % C << '\n'
         << A * B % C << '\n'
         << (A % C * (B % C)) % C;
  }
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

  ```cpp
  #include <iostream>
  using namespace std;
  int A, B;
  int main()
  {
  	cin >> A >> B;
  	cout << B % 10 * A << '\n'
  		<< B / 10 % 10 * A << '\n'
  		<< B / 100 * A << '\n'
  		<< B * A;
  }
  ```


