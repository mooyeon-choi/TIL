# 기술면접 대비

## 목차

1. [브라우저](#브라우저는-어떻게-동작하는가)
2. [네트워크](#네트워크)
3. [OOP](#oop)
4. [함수형 프로그래밍(Function Programming)](#함수형-프로그래밍function-programming)
5. [OOP vs 함수형 프로그래밍](#oop-vs-함수형-프로그래밍)
6. [JavaScript](#javascript)
7. [보안](#보안)

## 브라우저는 어떻게 동작하는가?

### 브라우저의 주요 기능

* 사용자가 선택한 자원을 서버에 요청하고 표시

  > 보통 HTML 문서지만 PDF나 이미지 또는 다른 형태일 수도 있다.
  >
  > 자원의 주소는 URI(Uniform Resource Identifier)에 의해 정해진다.

* HTML과 CSS 명세에 따라 HTML 파일을 해석해서 표시

  > 웹 표준화 기구인 W3C(World Wide Web Consortium)에서 정한다 최근에는 WHATWG(Web Hypertext Application Technology Working Group)와 함께 내놓은 MOU를 통해 합의하여 정한다.



### 브라우저의 기본 구조

1. 사용자 인터페이스 - 주소 표시줄, 이전/다음 버튼, 북마크 메뉴 등. 요청한 페이지를 보여주는 창을 제외한 나머지 모든 부분이다.
2. 브라우저 엔진 - 사용자 인터페이스와 렌더링 엔진 사이의 동작을 제어.
3. 렌더링 엔진 - 요청한 콘텐츠를 표시. 예를 들어 HTML을 요청하면 HTML과 CSS를 파싱하여 화면에 표시함.
4. 통신 - HTTP 요청과 같은 네트워크 호출에 사용됨. 이것은 플랫폼 독립적인 인터페이스이고 각 플랫폼 하부에서 실행됨.
5. UI 백엔드 - 콤보 박스와 창 같은 기본적인 장치를 그림. 플랫폼에서 명시하지 않은 일반적인 인터페이스로서, OS 사용자 인터페이스 체계를 사용.
6. 자바스크립트 해석기 - 자바스크립트 코드를 해석하고 실행.
7. 자료 저장소 - 이 부분은 자료를 저장하는 계층이다. 쿠키를 저장하는 것과 같이 모든 종류의 자원을 하드 디스크에 저장할 필요가 있다. HTML5 명세에는 브라우저가 지원하는 '[웹](http://www.html5rocks.com/en/features/storage)[ ](http://www.html5rocks.com/en/features/storage)[데이터](http://www.html5rocks.com/en/features/storage)[ ](http://www.html5rocks.com/en/features/storage)[베이스](http://www.html5rocks.com/en/features/storage)'가 정의되어 있다.

![brouser1](https://d2.naver.com/content/images/2015/06/helloworld-59361-1.png)

> 크롬은 대부분의 브라우저와 달리 각 탭마다 별도의 렌더링 엔진 인스턴스를 유지하여 각 탭은 독립된 프로세스로 처리된다.

### Localstorage vs. Sessionstorage vs. Cookies



## 네트워크

### HTTP와 HTTPS

### 3 way handshake

### TCP와 UDP

### OSI 7계층

### SSL란?

### RESTful이란?

### HTTP/1.1 vs HTTP/2



## OOP

### 객체 지향 프로그래밍이란 무엇인가?

> 컴퓨터 프로그램을 "객체(Object)"들의 모임으로 파악하고자 하는 프로그래밍의 패러다임 중 하나, 각 "객체(Object)" 들은 서로 메시지를 주고 받을 수 있으며 데이터를 처리할 수 있다.

#### 객체 지향 프로그래밍의 장점

> 기본적으로 강한 응집력(Strong Cohesion)과 약한 결합력(Weak Coupling)을 지향한다.
>
> * 응집력(Cohesion) : 프로그램의 한 요소가 해당 기능을 수행하기 위해 얼마만큼의 연관된 책임과 아이디어가 뭉쳐있는지를 나타내는 정도. 프로그램의 한 요소가 특정 목적을 위해 밀접하게 연관된 기능들이 모여서 구현되어 있고, 지나치게 많은 일을 하지 않으면 그것을 응집력이 높다고 표현한다.
> * 결합력(coupling): 프로그램 코드의 한 요소가 다른 것과 얼마나 강력하게 연결되어 있는지, 얼마나 의존적인지를 나타내는 정도. 결합력이 낮다는 것은 한 요소가 다른 요소들과 관계를 크게 맺고 있지 않은 상태를 의미한다.

* 프로그램을 유연하고 변경이 용이하게 만든다.
* 프로그램의 개발과 보수를 간편하게 만든다.
* 직관적인 코드 분석을 가능하게 한다.

#### OOP의 기본 구성 요소

* 클래스(Class)

  같은 종류의 집단에 속하는 속성과 행위를 정의한 것. 다른 클래스와 독립적으로 디자인해야 한다.

* 객체(Object)

  클래스의 인스턴스(Instance). 상위 클래스의 속성을 가지고 있으면서 개별적인 특성과 행위(Method) 또한 가지고 있다.

* 메서드(Method)

  클래스로부터 생성된 객체를 사용하는 방법. 객체의 속성을 조작하는 데 사용된다.

#### OOP의 특성

* 캡슐화

  객체의 데이터를 외부에서 직접 접근하지 못하게 막고, 함수를 통해서만 조작이 가능하게 하는 작업

* 추상화

  객체들이 가진 공통의 특성들을 파악하고 불필요한 특성들을 제거하는 과정

* 재사용성

  한 번 작성된 코드를 활용하여 동일한 객체를 만들 수 있다.



## 함수형 프로그래밍(Function Programming)

### 함수형 프로그래밍이란?

>  더 안정적인 프로그램을 만들기 위해 입력과 출력이 철저히 통제된 순수 함수 및 부수효과(Side-effect)를 최소화한 함수 위주로 프로그래밍 하는 것. 이를 통해 간결하고 가독성 높은 프로그램을 작성 할 수 있으며 동시성 작업을 더 안전하게 구현할 수 있다.
>
> * 부수 효과: 외부의 상태를 변경하는 것 또는 함수로 들어온 인자의 상태를 직접 변경하는 것
> * 순수 함수: 부수 효과가 없는 함수. 즉, 어떤 함수에 동일한 인자를 주었을 때 **항상 같은 값을 리턴하는 함수**

## OOP vs 함수형 프로그래밍

* 일급 객체의 차이

  * OOP: 클래스(Class) 또는 객체(Object)가 일급 객체가 된다.
  * 함수형 프로그래밍: 함수(Function) 자체가 일급 객체가 된다. (Kotlin)

  > 일급 객체란?
  >
  > 다음 3가지 조건을 충족할 경우 1급 객체라고 한다.
  >
  > 1. 변수나 데이타에 할당 할 수 있어야 한다.
  > 2. 객체의 인자로 넘길 수 있어야 한다.
  > 3. 객체의 리턴값으로 리턴할 수 있어야 한다.



## 비동기 프로그래밍

### AJAX(Asynchronous JavaScript and XML)

> 비동기적 JavaScript와 XML
>
> JavaScript를 이용해서 비동기적으로 서버와 브라우저가 데이터를 주고 받는 방식
>
> XML과 JSON 모두 사용한다.

* GET vs POST

  * GET

    요청을 전송할 때 필요한 데이터를 Body에 담지 않고, 쿼리스트링을 통해 전송한다.

    > 쿼리스트링
    >
    > URL의 끝에 `?`와 함께 이름과 값으로 쌍을 이루는 요청 파라미터를 쿼리스트링이라고 부른다. 만약, 요청 파라미터가 여러개이면 `&`로 연결한다. 쿼리스트링을 사용하게 되면 URL에 조회 조건을 표시하기 때문에 특정 페이지를 링크하거나 북마크할 수 있다.
    >
    > 예시) https://URL.com/resources?name1=value1&name2=value2

  * POST

    전송해야할 데이터를 HTTP 메시지의 Body에 담아서 전송한다. HTTP 메시지의 Body는 길이의 제한없이 데이터를 전송할 수 있으므로 GET과 달리 대용량 데이터를 전송할 수 있다. 또한 데이터가 Body로 전송되고 내용이 눈에 보이지 않아 GET보다 보안적인 면에서 안전하다고 생각할 수 있지만, POST 요청도 내용을 확인할 수 있기 때문에 민감한 정보는 반드시 암호화해 전송해야 한다.

    사용시 `Header`의 `Content-Type`에 요청 데이터의 타입을 표시해야 한다. 타입을 표시하지 않으면 서버는 내용이나 URL에 포함된 리소스의 확장자명 등으로 데이터 타입을 유추하고 만약 알 수 없는 경우에는 `application/octet-stream`로 요청을 처리한다.

  * GET과 POST의 차이

    > GET은 Idempotent, POST는 Non-idempotent하게 설계되어있다.
    >
    > * Idemptent(멱등)이란?
    >
    >   수학이나 전산학에서 연산의 한 성질을 나타내는 것으로,



## JavaScript

### JavaScript의 원시 타입(Primitive Data Type)

* Boolean 

  `true`와 `false`

* Null

* Undefined

* Number

  **정수만을 표현하기 위한 특별한 자료형은 없다.** 

### var, let, const

### 호이스팅

* `function`과 `var`에서 볼 수 있다. 함수 혹은 변수의 선언을 최상단으로 끌어올려주어 선언 위치보다 먼저 호출하더라도 사용할 수 있게 해준다.

  > 단, 함수 호이스팅은 선언 방식이 함수 선언식(Function declarrations) 인 경우에만 적용된다.

  ```javascript
  // 함수 선언식(function declarations)
  function funcName() {}
  
  // 함수 표현식(function expressions)
  var funcName = function() {}
  ```

### this



## 보안

### SOP

### CSRF와 XSS



