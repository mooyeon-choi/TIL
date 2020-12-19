/*
    Array helper methods
*/

/*
    Array.forEach
*/

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

// 실습, 높이*넓이값을 areas에 넣기
const images = [
  { height: 30, width: 20 },
  { height: 100, width: 100 },
  { height: 10, width: 5 },
];

let areas = [];

images.forEach(function (image) {
  areas.push(image["height"] * image["width"]);
});
console.log(areas);

/*
    map
    : 콜백함수의 return 결과를 각각 원소로 하는 **배열**을 **리턴**
*/
let numbers = [1, 2, 3];
let doubleNumbers = numbers.map(function (number) {
  return number * 2;
});
console.log(doubleNumbers);

let numbers = [1, 2, 3];
let doubleNumbers = numbers.map((number) => number * 2);
console.log(doubleNumbers);

// 실습
const images = [
  { height: 30, width: 20 },
  { height: 100, width: 100 },
  { height: 10, width: 5 },
];

images.map(function (image) {
  return image.height * image.width;
});
images.map((image) => image.height * image.width);

/*
    filter
    : callback 함수의 **return 결과**가 참인 것을 각각 원소로 하는 배열을 **리턴**
*/
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

// 실습. 과일만 담기
let products = [
  { name: "banana", type: "fruit" },
  { name: "tomato", type: "vegetable" },
  { name: "apple", type: "fruit" },
  { name: "cucumber", type: "vegetable" },
];

let bag = products.filter(function (product) {
  return product.type === "fruit";
});
let bag2 = products.filter((product) => product.type === "fruit");

/*
    reduce(callbackfn, initialvalue)
    : return 결과를 누적한 결과를 return
*/
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

/*
    find : 일치하는 첫번째 원소를 return.
*/
mySsafy.find(function (score) {
  return score === 90;
});

// 연습. 나이가 30인 사람
let heros = [
  { name: "헐크", age: 100 },
  { name: "아이언맨", age: 50 },
  { name: "스파이더맨", age: 30 },
];

heros.find(function (hero) {
  return hero.age === 30;
});
heros.find((hero) => hero.age === 30);

/*
    some, every
*/
// some: return을 만족하는게 하나라도 있느냐
let myNumbers = [1, 2, 3, 4];
myNumbers.some(function (number) {
  return number % 2 === 0;
});
// every: 모든 것이 return을 만족하느냐
myNumbers.every(function (number) {
  return number % 2 !== 0;
});
