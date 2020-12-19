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
