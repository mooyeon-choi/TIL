# JavaScript

```
페이지📄를 동적으로 만들어주기 위해 필요한 JavaScript!!
그 사용법을 낱낱이 파해쳐보자!
```

## 목차

* [Variable](#variable)
* [Hoisting](#hoisting)
* [Type](#type)
* [Operator](#operator)
* [Flow](#flow)
* [Function](#function)

## Variable

> var
>
> let / const

* [코드로 보기](./variable.js)

1. 선언과 할당

   * `var`

     ```js
     var myVar; // 선언
     myVar = 1; // 할당
     var myVar = "Hello"; // 재선언 가능
     ```

   * `let`

     ```js
     let myLet; // 선언
     myLet = 2; // 할당
     myLet = 3; // 재할당 가능
     let myLet = "hi" // SyntaxError -> 이미 선언됨
     ```

   * `const`

     ```js
     const myConst // SyntaxError -> 초기화 누락
     const myConst = "hi"; // 반드시 값과 함께 선언
     myConst = "bye" // TypeError -> 재할당 불가
     ```

2. Scope

   * `var`

     ```js
     let VarFunction = function () {
         var myVar = 0;
         if (true) {
             var myVar = 1;
             console.log(myVar); // 1
         }
         console.log(myVar); // 1
     };
     ```

   * `let`

     ```js
     let LetFunction = function () {
         let myLet = 0;
         if (true) {
             let myLet = 1;
             console.log(myLet); // 1
         }
         console.log(myLet); // 0
     }
     ```

## Hoisting

* [코드로 보기](./hoisting.js)

* `var`

  ```js
  console.log(mooyeon); // undefined
  var mooyeon = "무연";
  ```

  위의 코드는 다음과 같이 이해한다.

  ```js
  var mooyeon; // hoisting
  console.log(mooyeon);
  mooyeon = "무연";
  ```

* `let`

  ```js
  console.log(dooly); // ReferenceError - 초기화하기 전 접근 금지
  let dooly = "둘리";
  ```

* 이해하기

  * `var`
    1. 선언과 동시에 초기화
    2. 할당

  * `let`, `const`

    TDZ(temporal Dead Zone)이 존재

    1. 선언
    2. TDZ
    3. 초기화
    4. 할당

## Type

> * 원시타입 (primitive data type)
>   * boolean
>   * null
>   * undefined
>   * number
>   * string
>   * symbol (ES6+)
> * 객체타입 (object)
>   * object

* [코드로 보기](./type.js)

1. Number

   ```js
   3 - 5;
   Infinity; // typeof Infinity >> "number"
   NaN; // typeof NaN >> "number" 산술 연산 불가, number가 아니라는 number..
   10 / 0; // Infinity
   0 / 0; // NaN
   ```

2. String

   ```js
   let myName = "무연";
   myName = '무연';
   // ` (backtick) : ES6+, 템플릿 리터럴
   // string interpolation, 줄바꿈(개행) - 엔터도 인식하여 출력된다.
   myName = `무
   연`;
   ```

3. Boolean

   ```js
   true;
   false;
   ```

4. Empty value

   ```js
   undefined; // typeof undefined >> "undefined"
   null; // typeof null >> "object"
   ```

## Operator

* [코드로 보기](./operator.js)

1. 동등 연산자 (`==`)

   ```js
   1 == '1'; // true
   ```

2. 일치 연산자 (`===`)

   ```js
   1 === '1' // false
   ```

3. 할당 

   * `=`, `+=`, `-=`, `*=`, `/=`, ...

4. 비교

   * `>`, `<`, `>=`, `<=`, ...

5. 논리

   * and : `&&`
   * or : `||`

6. Not (`!`)

7. 삼항연산자 표현식

   `? true : false`

   ```js
   2 > 4 ? true : false
   ```

## Flow

* [코드로 보기](./flow.js)

1. if문

   ```js
   if (userName === "ssafy") {
     message = "<h1>Hello ssafy</h1>";
   } else if (userName === "1q2w3e4r") {
     message = "<h1>Admin page입니다</h1>";
   } else {
     message = `<h1>${userName} 환영합니다.</h1>`;
   }
   ```

2. switch문

   ```js
   switch (userName) {
     case "1q2w3e4r": {
       message = "<h2>관리자님 충성충성</h2>";
       break;
     }
     case "ssafy": {
       message = '<a href="http://edu.ssafy.com">싸피</a>';
       break;
     }
     default: {
       message = `<h1>${userName} 환영합니다.</h1>`;
     }
   }
   ```

3. for문

   ```js
   /*
       *반복문
       var는 함수스코프를 가지고 있어서 for문 이후에 i 변수에 값이 유지
       let은 블록스코프를 가지고 있어서 for문 이후에 해당 변수는 없음.
   */
   for (var i = 0; i < 3; i++) {
     console.log(i);
   }
   console.log(i); // 3
   
   for (let i = 0; i < 3; i++) {
     console.log(i);
   }
   console.log(i); // ReferenceError
   ```

   ```js
   let myArray = ["무연", "현택", "순범"];
   for (let name of myArray) {
     document.write(name);
   }
   ```

## Function

* [코드로 보기](./function.js)

* 선언식과 표현식

  ```js
  console.log(myAdd(2, 3)); // 5
  console.log(myAdd2(3, 5)); // ReferenceError: myAdd2 is not defined
  
  // 선언식 -> hoisting 된다
  function myAdd(a, b) {
    return a + b;
  }
  
  // 표현식 -> hoisting 안되니 웬만하면 표현식으로 함수 만들자.
  let myAdd2 = function (a, b) {
    return a + b;
  };
  ```

* Arrow function

  ```js
  let myFunction = function (a) {
    return a + 1;
  };
  // 1. function 키워드 삭제 후 =>
  let myArrowFunction1 = a => {
    return a + 1;
  };
  // 1-1. 인자가 하나라면, 소괄호 생략 가능
  // 1-2. 문장이 한 줄이고, 리턴이라면 중괄호 및 return 키워드 생략 가능
  let myArrowFunction2 = (a) => a + 1;
  // 1-3. 인자가 없는 경우에는 () or _
  let ArrowGreeting2 = () => {
    console.log("happy!");
  };
  ```

* 기본 인자

  ```js
  let greeting2 = (name = "타키") =>
    name(
      /*
       * 익명함수
       */
      (function (a) {
        return a * 10;
      })(10)
    )((a) => a + 10)(10);
  ```

  



