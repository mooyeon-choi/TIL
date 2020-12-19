/*
 * 함수
 */
console.log(myAdd(2, 3));
console.log(myAdd2(3, 5));

// 선언식 -> hoisting 된다
function myAdd(a, b) {
  return a + b;
}

// 표현식 -> hoisting 안되니 웬만하면 표현식으로 함수 만들자.
let myAdd2 = function (a, b) {
  return a + b;
};

/*
    * arrow function 
    ES6+
*/

let myFunction = function (a) {
  return a + 1;
};
// 1. function 키워드 삭제 후 =>
let myArrowFunction1 = (a) => {
  return a + 1;
};
// 1-1. 인자가 하나라면, 소괄호 생략 가능
// 1-2. 문장이 한 줄이고, 리턴이라면 중괄호 및 return 키워드 생략 가능
let myArrowFunction2 = (a) => a + 1;

// 연습1. 제곱의 결과를 나타내는 square 함수
let square = function (num) {
  return num ** 2;
};
let ArrowSquare1 = (num) => {
  return num ** 2;
};
let ArrowSquare2 = (num) => {
  return num ** 2;
};
let ArrowSquare3 = (num) => num ** 2;

let greeting = function () {
  console.log("happy!");
};

let ArrowGreeting1 = () => {
  console.log("happy!");
};
// 1-3. 인자가 없는 경우에는 () or _
let ArrowGreeting2 = (_) => {
  console.log("happy!");
};

// 1-4. 기본인자
let greeting2 = (name = "타키") =>
  name(
    /*
     * 익명함수
     */

    (function (a) {
      return a * 10;
    })(10)
  )((a) => a + 10)(10);
