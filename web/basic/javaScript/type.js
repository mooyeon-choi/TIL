/*
* 원시타입 (primitivie data type)
    - boolean
    - null
    - undefiened
    - number
    - sring
    - symbol (ES6+)
* 객체타입 (object)
    - object
*/

// number
3 - 5;
Infinity; // typeof Infinity >> "number"
NaN; // typeof NaN >> "number" 산술 연산 불가, number가 아니라는 number...
10 / 0; // Infinity
0 / 0; // NaN

// string
let myName = "무연";
myName = "무연";
// ' (backtick) : ES6+, 템플릿 리터럴
// string interpolation, 줄바꿈(개행) - 엔터도 인식하여 출력된다.
myName = `무
연`;

console.log(`안녕하세요, ${myName} 입니다.`);

// boolean
true;
false;

// empty value
undefined; // typeof -> undefined
null; // typeof -> object
