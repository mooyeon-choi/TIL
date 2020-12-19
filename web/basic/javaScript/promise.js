// 데이터를 외부로 부터 받아와서 변수에 저장하고 출력하는 함수를 만들어보자!

// 1. 비동기가 없는 상태의 코드
function getData() {
  const data = { data: "some data" };
  return data;
}

let response = getData();
console.log(response);
// 이건 콜백하고 그런게 아니니까 정상작동하겠지

// 2. setTimeout
function getData() {
  let data;
  setTimeout(function () {
    console.log("요청을 보냈습니다.");
    data = { data: "some data" };
  }, 1000);
  return data;
}
let response1 = getData();
console.log(response1);
// data는 그럼 어디로 가는가!

// 위의 것을 해결하기 위한 방법으로
// 3. callback func 정의!
function getDataCallback(callback) {
  setTimeout(function () {
    console.log("요청을 보냈습니다");
    const data = { data: "some data" }; // 데이터 도착! 하면
    callback(data); // 이때! 내가 원하는 작업(data담아서 출력)을 시작!
  }, 1000);
}
// 함수 호출. 인자로 '함수'를 넘겨주는데, 그게 출력하는 작업을 하는 함수. 얘~를 나중에 callback 하겠다..!
getDataCallback(function (data) {
  let response2 = data;
  console.log(response2);
});
// 그런데 이건 콜백지옥을 만든다...

// 그래서 나온 것이!
// 4. promise (약속)
function getDataPromise() {
  // Promise 오브젝트를 리턴하는 이런게 생겼다
  return new Promise((resolve) => {
    setTimeout(function () {
      console.log("요청을 보냈습니다");
      const data = { data: "some data" };
      resolve(data);
    }, 1000);
  });
}

let response3 = getDataPromise();
// 이러면 response3에 promise 오브젝트가 리턴된다고!
console.log(response3); // 1. 출력은 pending이라고 된다. (요청처리중..?)
console.log(response3); // 2. 이제 출력이 resolved라고 된다. (resolve했어, 함수 호출했어 상태)
// 그러면 resolved 뭐 이렇게 담기는데 그것을 풀어주는 것이 .then
response3.then((response) => console.log(response)); // 3. data 출력
// 그래서 다음과 같이 쓸 수 있다.
getDataPromise().then((response) => console.log(response));
// 이것 덕분에 .then .then .then 하면서 작업을 진행할 수 있게 되었다

// 4-1. Promise 추가내용
function myPromise(url) {
  return new Promise((resolve, reject) => {
    // resolve 하나만 아니라 reject도 같이 넣을 수 있는데
    if (url === "http") {
      resolve("성공");
    } else {
      reject("url이 잘못되었습니다.");
    }
  });
}
const promise1 = myPromise("http");
console.log(promise1);
const promise2 = myPromise("www");
console.log(promise2);
// resolve로 가면 그 다음으로 .then으로 가고
// reject로 가면 그 다음으로 .catch로 간다. (아무리 .then이 많아도 creject로 가면 .then은 무시한다는 말)
promise2
  .then((response) => {
    // 이 부분은 실행이 안된다고!
    console.log("성공");
    console.log(response);
  })
  .catch((error) => {
    console.log("error");
    console.log(error);
  });

// chaining !
function getDataPromise() {
  // Promise 오브젝트를 리턴하는 이런게 생겼다
  return new Promise((resolve) => {
    setTimeout(function () {
      console.log("요청을 보냈습니다");
      const data = { data: "some data" };
      resolve(data);
    }, 1000);
  });
}
getDataPromise()
  .then((response) => {
    // response = data
    console.log(response); // {'data': 'some data'}
    return response.data; // 'some data'
  })
  .then((data) => {
    // data = 'some data'
    console.log(data); // 'some data'
  })
  .catch((error) => {
    console.log(error);
  });

// chaining
axios
  .get("https://jsonplaceholder.typicode.com/posts/1")
  .then((response) => {
    return response.data.userId; // 실제로는 promise object로 포장되어 리턴
  })
  .then((userId) => {
    return axios.get(`https://jsonplaceholder.typicode.com/users/${userId}`);
  })
  .then((response) => {
    console.log(response);
    console.log(response.data.name);
  });

// 5. async / await -> 동기 작업인척 하기!!!가 핵심.  + promise (promise가 리턴인 함수를 대상으로만 가능하다.)
function getDataPromise() {
  // Promise 오브젝트를 리턴하는 이런게 생겼다
  return new Promise((resolve) => {
    setTimeout(function () {
      console.log("요청을 보냈습니다");
      const data = { data: "some data" };
      resolve(data);
    }, 1000);
  });
}
async function printData() {
  const response = await getDataPromise();
  console.log(response);
}
printData(); // {data: "some data"}

// 위에서 jsonplceholder를 이렇게 할 수 있따.!
// 동기처럼... 코드를 짤 수 있지...? 또 장점이... 오류 시점이 더 정확하게 나온다...
async function printUser() {
  try {
    // resolve 호출 되면.
    const response = await axios.get(
      "https://jsonplaceholder.typicode.com/posts/1"
    );
    const userId = response.data.userId;
    console.log(userId);
  } catch (error) {
    console.log(error); // rejected 호출되면.
  }
}
printUser();
