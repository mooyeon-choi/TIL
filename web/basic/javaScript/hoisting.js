console.log(mooyeon); // undefined
var mooyeon = "무연";

/* 위의 코드를 js는 다음과 같이 이해한다.
var taewoo  // hoisting
console.log(taewoo)
taewoo = '김태우'
*/

console.log(dooly); // ReferenceError - 초기화하기 전 접근 금지
let dooly = "둘리";

/*
var
1. 선언과 동시에 초기화
2. 할당
let, const는 TDZ(Temporal Dead Zone)이 존재.
1. 선언
2. TDZ
3. 초기화 
4. 할당
*/
