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
