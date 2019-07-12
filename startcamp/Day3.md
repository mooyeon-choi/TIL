
# Day3

## 파이썬 기본 코딩 예제

### 문제1 (문자열 처리)

1. 문자열을 입력받아 문자열의 첫 글자와 마지막 글자를 출력하는 프로그램을 작성하시오

   ```python
   string = input('문자를 입력하세요: ')
   print(f'첫글자: {string[0]}\n마지막글자: {string[-1]}' )
   ```

   > str은 기본 함수이므로 변수명을 생성할때 겹치지 않도록 주의한다

   * 문자열 변수
   * `string[+]` : 문자열의 앞부분부터 
   * `string[-]` : 문자열의 뒷부분부터
   * `input()` : 입력값을 `string` 으로 받아온다.

### 문제2 (for문 응용)

2.  자연수 N이 주어졌을 때, 1부터 N까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오

   ```python
   numbers = int(input('숫자를 입력하세요: '))
   # range(1, numbers+1)도 가능
   for number in range(numbers):
       print(number+1)
   ```

   * `range()` : `0`에서 부터 시작하므로 `+1`을 따로 추가해준다.
   * `int(input('숫자를 입력하세요: '))` : 입력값을 `integer`값으로 변환해준다.

### 문제3 (비교, 논리 연산자)

3. 숫자를 입력 받아 짝수/홀수를 구분하는 코드를 작성하시오

   ```python
   number = int(input('숫자를 입력하세요: '))
   if number % 2:
       print('홀수 입니다.')
   else:
       print('짝수 입니다.')
   ```

   > `True = 1`, `False = 0` 과 같으므로 `0` 또는 `1` 로 나타나는 값의 경우 비교문을 추가하지 않아도 정상적으로 동작한다.


### 문제4 (논리 연산자)

3. 표준 입력으로 국어, 영어, 수학, 과학 점수가 입력됩니다.

   국어는 90점 이상,

   영어는 80점 초과,

   수학은 85점 초과, 

   과학은 80점 이상일 때 합격이라고 정했습니다.(한 과목이라도 조건에 만족하지 않으면  불합격)

   다음 코드를 완성하여 합격이면 True, 불합격이면 False가 출력되도록 작성하시오. 

   ```python
   a = int(input('국어: '))
   b = int(input('영어: '))
   c = int(input('수학: '))
   d = int(input('과학: '))
   # 위의 4줄의 주석을 풀고 아래에 코드를 작성해 주세요.
   if a >= 90 and b > 80 and c > 85 and d >= 80:
       print(True)
   else:
       print(False)
   ```

   > `and` , `or` 과 같은 논리 연산자를 이용해 한번에 표현할 수 있다.


### 문제5  (리스트 정렬)

3. 표준 입력으로 물품 가격 여러 개가 문자열 한 줄로 입력되고, 각 가격은 ;(세미콜론)으로 구분되어 있습니다.

   입력된 가격을 높은 가격순으로 출력하는 프로그램을 만드세요.

   입력 예시: `300000;20000;10000`

   ```python
   prices = input('물품 가격을 입력하세요: ')
   prices = prices.split(';')
   # 1. 반복문
   int_price = []
   for price in prices:
       int_price.append(int(price))
   print(int_price)
   # 2. list comprehension
   int_price2 = [int(price) for price in prices]
   print(int_price2)
   # 3. map
   int_price3 = list(map(int, prices))
   int_price3 = sorted(int_price3, reverse=True) 
   # int_price3.sort()            
   for number in int_price3:
       print(number)
   ```

   * `반복문 ` : 새로운 리스트를 생성하고 `.append()` 를 통해 리스트의 변수 하나하나 추가해주어 사용하는 방법

   * `list comprehension ` :  리스트를 선언함과 동시에 `[]` 안에 `for` 문을 넣어 위의 과정이 바로 실행되도록 하는 방법

   * `map` : 첫번째 인자의 함수를 두번째 인자를 반복하며 적용

     * 반복 가능한 객체에 함수를 각각 적용한다.

## HTML/CSS

### HTML

`HTML` 은 HyperText Markup Language의 약자로 웹 문서를 구조화 하는데 사용되는 언어이다.

#### 1. HTML 기본 구조

   ```html
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <meta http-equiv="X-UA-Compatible" content="ie=edge">
       <title>Document</title>
   </head>
   <body>
       <h1>용흠아 안녕!</h1>
   </body>
   </html>
   ```

   * `<head> </head>` 는 문서의 정보를 담고 있다.
   * `<body> </body>` 는 문서의 본문을 담고 있다.

#### 2. 태그의 종류

   1. 기본적으로 태그는 `여는태그` 와 `닫는태그` 로 구성된다

      ```html
      <h1>제목1</h1>
      ```

   2. `닫는태그` 가 없는 경우도 있다. (self-closing tag)

      ```html
      <img src="__"/>
      ```

#### 3. 태그의 구성

   ```html
   <img src="___" width="300" height="300"/>
   <a href="https://google.com" class="blue">구글</a>
   ```

   * 태그별로 공통적으로 가질 수 있는 속성 : `id` , `class` , `style`
   * 각 태그별로 가질 수 있는 속성이 추가적으로 있다.
     * img - `src` , `width` , `height`
     * a - `href`



### CSS

CSS는 Cascading Style Sheets의 약자로, HTML을 꾸며주는 역할을 한다.

HTML을 꾸며주기 위하여, `선택자(selector)` 를 통해 특정한 element를 지정하여야 한다.

#### 1. 선택자

   * 태그 선택자

     ```css
     p {
         color: red;
     }
     ```

   * class 선택자

     ```css
     .blue {
         color: blue;
     }
     ```

   * id 선택자

     ```css
     #pink {
         color: pink;
     }
     ```

   선택자 우선순위는 id선택자 > class선택자 > 태그선택자 순서로 적용된다.



### Flask

`Flask` 는 파이썬 기반의 micro framework이다.

#### 1. 설치

   ```bash
   $ pip install flask
   ```

#### 2. 기본 코드

   ```python
   from flask import Flask
   
   app = Flask(__name__)
   
   @app.route('/')
   def hello():
       return 'Hello!'
   
   if __name__ == '__main__':
       app.run(debug=True)
   ```

#### 3. 서버 실행

   ```bash
   $ flask run
   ```

   * 기본적으로 `flask run` 명령어는 `app.py` 파일을 실행시킨다. 만약 다른 파일명으로 만들었다면, 옵션을 추가해야 한다.

   * 마지막 두줄을 작성해놓았다면, 아래와 같이 실행도 가능하다.

     ```bash
     $ python app.py
     ```

## Variable routing

요청 오는 url을 변수화 하여 값을 사용할 수 있다.

```python
@app.route('/hi/<string:name>')
def hi(name):
    return f'{name}아 안녕?'
```

## Rendering Template

`HTML` 파일을 만들어 활용할 수 있다. 기본적으로 `templates` 폴더에 파일을 만들어야 한다.

```
app.py
templates/
	hi.html
	lunch.html
	index.html
```

```python
from flask import Flask, render_template
# ...
@app.route('/hi')
def hi():
    return render_template('hi.html')
```

`HTML` 파일에서 변수의 값을 출력하고자 한다면, 키워드 인자로 그 값을 넘겨줘야한다.

```python
return render_template('hi.html', name=name)
```

그리고 출력을 위해서는 `{{ }}` 사용한다.

```jinja2
<h1>{{name}} 안녕?</h1>
```

## Flask Template Engine - jinja2

Flask는 기본적으로 Template을 만들때 `jinja2` 언어를 사용한다. 기본 문법은 다음과 같다.

1. 값 출력

   ```jinja2
   <h1> {{ name }}, 안녕? </h1>
   ```

2. 조건문

   ```jinja2
   {% if name == '용흠' %}
   	<h1>반장님 안녕하세요.</h1>
   {% else %}
   	<h1>학생들 ㅎㅇ</h1>
   {% endif %}
   ```

3. 반복문

   ```jinja2
   {% for menu in menu_list %}
   	<li>{{ menu }}</li>
   {% endfor %}
   ```


## Form data

HTML에서 사용자로 부터 정보를 받기 위해서는 `Form` 태그를 활용한다.

### Form 태그 기본 구조

```html
<!-- templates/ping.html -->
<Form action="/pong(__url)">
    <input type="text" name="say">
    <input type="radio" name="gender" value="M">남자
    <input type="radio" name="gender" value="F">여자
    <input type="submit" name="전송">
</Form>
```

* `form` 태그는 `action` 속성으로 해당 폼이 전송될 `url`을 지정해야 한다.
* `form` 태그 내에는 `input` 태그를 정의하며, 사용자에게 받을 정보를(설문지를 만든다.) 만들어 놓는다. 
* `input` 태그에는 어떤 종류의 입력을 받을지 `(type)`와 어떤 변수에 담아서 보낼지`(name)` 정의한다.

### Flask에서 사용자로부터 정보 받기

1. 사용자가 입력할 수 있는 `form` 보여주기

   ```python
   # app.py
   @app.route('/ping')
   def ping():
       return render_template('ping.html')
   ```

   ```html
   <!-- templates/ping.html -->
   <Form action="/pong(__url)">
       <input type="text" name="say">
       <input type="submit" name="전송">
   </Form>
   ```

2. 정보 받아서 활용하기

   ```python
   # app.py
   from flask import Flask, render_template, request
   @app.route('/pong')
   def pong():
       request.args.get('say')
       return render_template('pong.html', say=say)
   ```

   ```html
   <!-- templates/pong.html -->
   <h1>{{ say }}!!!!</h1>
   ```

   * `request.args` 는 일종의 `dictionary` 이고, `key` 는 input에 정의한 `name` 이고 사용자가 입력한 값은 `value` 이다.




