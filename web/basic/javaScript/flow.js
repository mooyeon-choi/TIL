let userName = prompt("넌 누구니!!");

let message;

// if
if (userName === "ssafy") {
  message = "<h1>Hello ssafy</h1>";
} else if (userName === "1q2w3e4r") {
  message = "<h1>Admin page입니다</h1>";
} else {
  message = `<h1>${userName} 환영합니다.</h1>`;
}

document.write(message);

//switch
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

document.write(message);

// while - python과 비슷하고

// for
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

let myArray = ["무연", "현택", "순범"];
for (let name of myArray) {
  document.write(name);
}
