# JavaScript

```
페이지📄를 동적으로 만들어주기 위해 필요한 JavaScript!!
그 사용법을 낱낱이 파해쳐보자!
```

## 목차

* [Variable](#variable)

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

     