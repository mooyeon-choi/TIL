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
* [Array](#array)
* [Object](#object)
* [Array helper method](#array-helper-method)
* [DOM](#dom)
* [Blocking](#blocking)

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

## Array

* [코드로 보기](./array.js)

1. Array 선언

   ```js
   let numbers = [10, 1, 3, 5];
   ```

2. Index 요소 접근

   ```js
   numbers[0]; // 10
   numbers[-1]; // undefined
   numbers.length; // 4
   ```

3. 뒤집기

   ```js
   numbers.reverse(); // return + 원본 변경.
   ```

4. 마지막에 원소 추가

   ```js
   numbers.push(20); // 마지막에 원소 추가 + return (길이)
   ```

5. 마지막 원소 제거 및 `return`

   ```js
   numbers.pop(); // 20 : 마지막 원소 pop + return (해당 원소)
   ```

6. 가장 앞에 원소 추가 및 길이 `return`

   ```js
   numbers.unshift(3); // 맨앞에 원소 추가 + return (길이)
   ```

7. 맨앞 원소 제거 및 `return`

   ```js
   numbers.shift(); // 맨앞 원소 제거 + return (해당 원소)
   ```

8. 포함 여부 확인

   ```js
   numbers.includes(1); // true : 포함여부 확인
   ```

9. 포함 여부 + 가장 먼저 존재하는 위치 반환

   ```js
   numbers.indexOf(1); // 가장 먼저 존재하는 위치
   ```

10. String으로 바꾸기

    ```js
    numbers.join(); // 기본이 ,
    numbers.join("-"); // -로 연결.
    ```

## Object

* [코드로 보기](./object.js)

* Object 생성

  ```js
  // 키값을 ""로 굳이 안묶어도 된다.
  const me = {
    // 프로퍼티
    name: "kim",
    "phone number": "01012345678",
    phone: {
      type: "iphone XS MAX",
    },
    // 메서드 function 키워드만 작성하자!
    greeting: function () {
      console.log(this); // me
      console.log(`hi ${this.name}`); // this : '나'를 뜻한다. self.name처럼
    },
    greeting2: () => {
      console.log(this); // 전역객체 window
      console.log(`hi ${this.name}`); // 이건 this가 안먹히네!? arrow function에서의 this는 무조건 상위 object! 나중가면 유용할걸!?
    },
  };
  ```

* 오브젝트 리터럴 (ES6+)

  ```js
  let book = "자바스크립트 완전 정복";
  let album = {
    IU: ["좋은날", "밤편지"],
    BTS: ["작은것들을 위한 시"],
  };
  // 위의 값들을 object에 넣으면 바로 key,value로 알아서 들어간다.
  let bag = {
    book,
    album,
  };
  ```

* JSON

  ```js
  // JSON (Javascript Object Notation - 자바스크립트 오브젝트 표기법)
  // JSON은 기본적으로 자바스크립트 오브젝트 표기법을 가진 "문자열"이다
  // object -> JSON
  let jsonData = JSON.stringify(me);
  let myObject = JSON.parse(jsonDate);
  ```

## Array helper method

* [코드로 보기](./array_helper_method.js)

* `Array.forEach`

  ```js
  let numbers = [1, 2, 3];
  
  // 1. 반복문 (for)
  for (let i = 0; i < numbers.length; i++) {
    console.log(numbers[i]);
  }
  
  // 2. 반복문 (for..of)
  for (let num of numbers) {
    console.log(num);
  }
  
  // 3. forEach
  numbers.forEach(function (num) {
    console.log(num);
  });
  ```

* `map`

  콜백함수의 return 결과를 각각 원소로 하는 **배열**을 **리턴**

  ```js
  let numbers = [1, 2, 3];
  let doubleNumbers = numbers.map(function (number) {
    return number * 2;
  });
  console.log(doubleNumbers);
  
  let numbers = [1, 2, 3];
  let doubleNumbers = numbers.map((number) => number * 2);
  console.log(doubleNumbers);
  ```

* `filter`

  callback 함수의 **return 결과**가 참인 것을 각각 원소로 하는 배열을 **리턴**

  ```js
  // images의 높이가 100보다 작은 object만 담은 배열
  // 반복문으로
  let list = [];
  for (image of images) {
    if (image.height < 100) {
      list.push(image);
    }
  }
  console.log(list);
  // filter로
  list = images.filter(function (image) {
    return image.height < 100;
  });
  console.log(list);
  ```

* `reduce(callbackfn, initialvalue)`

  return 결과를 누적한 결과를 return

  ```js
  let mySsafy = [100, 100, 95, 90];
  let total = 0;
  mySsafy.forEach(function (score) {
    total += score;
  });
  
  mySsafy.reduce(function (total, score) {
    // total: 누적, score: 각 원소
    return total + score;
  }, 10000); // 10000 :초기값,  reduce의 두번째 인자. 없으면 첫 score부터 시작해서 return
  
  mySsafy.reduce((total, score) => total + score, 10000);
  ```

* `find`

  일치하는 첫번째 원소를 return.

  ```js
  mySsafy.find(function (score) {
    return score === 90;
  });
  ```

* `some`, `every`

  ```js
  // some: return을 만족하는게 하나라도 있느냐
  let myNumbers = [1, 2, 3, 4];
  myNumbers.some(function (number) {
    return number % 2 === 0;
  });
  // every: 모든 것이 return을 만족하느냐
  myNumbers.every(function (number) {
    return number % 2 !== 0;
  });
  ```

## DOM

* [코드로 보기](./dom.html)

```html
<body>
  <h1 class="text">DOM 조작(Document Object Model)</h1>
  <h2 class="text">카페</h2>
  <img src="my.png", alt="">
  <ul id='my-list'>
    <li>아메리카노</li>
    <li>자바칩프라프치노</li>
  </ul>
</body>
```

## Blocking

* [코드로 보기](./blocking.js)

* `setTimeout`과 Callback

  ```js
  function a() {
    console.log("a");
  }
  console.log("hi");
  setTimeout(a, 3000);
  console.log("bye"); // hi -> bye -> (3초뒤) -> a
  
  function printHello() {
    console.log("Hello");
  }
  
  function baz() {
    console.log("baz"); // 1
    setTimeout(printHello, 3000); // 3- 비동기로 동작하는 함수이다. 3000이 아니라 0이어도 Hello가 마지막에 출력된다..!!
    console.log("baz end"); //2
  }
  
  function bar() {
    console.log("bar");
    baz();
  }
  
  function foo() {
    console.log("foo");
    bar();
  }
  
  foo();
  
  function sum(x, callbackfn) {
    setTimeout(callbackfn, 1000, x + 1);
  }
  var result = 0;
  sum(2, function (x) {
    result = x;
    console.log(result); // 3
  });
  console.log(result); // 0
  ```

