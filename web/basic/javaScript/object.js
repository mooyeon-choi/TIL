// 파이썬과 다르게 키값을 ''로 굳이 안묶어도 된다.
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

console.log(me.name);
console.log(me["name"]);
console.log(me.phone.type);

// ES6+ 오브젝트 리터럴
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

// JSON (Javascript Object Notation - 자바스크립트 오브젝트 표기법)
// JSON은 기본적으로 자바스크립트 오브젝트 표기법을 가진 "문자열"이다
// object -> JSON
let jsonData = JSON.stringify(me);
let myObject = JSON.parse(jsonDate);

// 지금까지 이렇게 객체로 만들어왔지

// 함수선언으로 우리가 익숙한 형태의 object 생성 가능
// 인자를 받아서 뭔가를 하는, 다양한 객체를 만들고 싶을 때.
// 다음과 같이 함수로 만들어 놓고 ''new'' 키워드로 불러와 객체 생성가능.
const Person = function (name, phone) {
  this.name = name;
  this.phone = phone;
  this.greeting = function () {
    return "hi" + this.name;
  };
};
const moo = new Person("최무연", "010-????-????"); // new! 특정한 오브젝트를 만드는 키워드
lee.name;
lee.greeting();

// 그럼 arrow func 으로도 될까?
const Animal = (name) => {
  this.name = name;
};
const dog = new Animal("dog"); // Error!!!!!!!!!
// 생성자 함수에서는 arrow func 사용 금지

// object 리터럴
const name = "겨레";
const phone = "010-0000-2222";
const greeting = function () {
  return "hi," + this.name;
};
const you = {
  name,
  phone,
  greeting,
};
//이런식으로 쓰는게 오브젝트 리터럴 방법. 축약형이다 라고 간단히 생각하면 된다.
