# Level 1 (JavaScript)

## 목차

* [크레인 인형뽑기 게임](#크레인-인형뽑기-게임)
* [두 개 뽑아서 더하기](#두-개-뽑아서-더하기)
* [완주하지 못한 선수](#완주하지-못한-선수)
* [K번째수](#k번째수)
* [2016년](#2016년)
* [3진법 뒤집기](#3진법-뒤집기)
* [가운데 글자 가져오기](#가운데-글자-가져오기)
* [같은 숫자는 싫어](#같은-숫자는-싫어)
* [나누어 떨어지는 숫자 배열](#나누어-떨어지는-숫자-배열)
* [두 정수 사이의 합](#두-정수-사이의-합)
* [문자열 내 마음대로 정렬하기](#문자열-내-마음대로-정렬하기)
* [문자열 내 p와 y의 개수](#문자열-내-p와-y의-개수)
* [문자열 내림차순으로 배치하기](#문자열-내림차순으로-배치하기)
* [문자열 다루기 기본](#문자열-다루기-기본)
* [서울에서 김서방 찾기](#서울에서-김서방-찾기)
* [수박수박수박수박수박수?](#수박수박수박수박수박수)
* [문자열을 정수로 바꾸기](#문자열을-정수로-바꾸기)
* [내적](#내적)
* [시저 암호](#시저-암호)
* [약수의 합](#약수의-합)
* [이상한 문자 만들기](#이상한-문자-만들기)
* [자릿수 더하기](#자릿수-더하기)
* [자연수 뒤집어 배열로 만들기](#자연수-뒤집어-배열로-만들기)
* [정수 내림차순으로 배치하기](#정수-내림차순으로-배치하기)
* [정수 제곱근 판별](#정수-제곱근-판별)
* [제일 작은 수 제거하기](#제일-작은-수-제거하기)
* [짝수와 홀수](#짝수와-홀수)
* [콜라츠 추측](#콜라츠-추측)
* [평균 구하기](#평균-구하기)

## 크레인 인형뽑기 게임

* [문제 링크](https://programmers.co.kr/learn/courses/30/lessons/64061?language=javascript)

* 풀이

  ```js
  function solution(board, moves) {
      var answer = 0;
      var basket = new Array();
      for (var i in moves) {
          for (var j=0; j < board.length; j++) {
              if (board[j][moves[i] - 1]) {
                  if (basket.length > 0) {
                      if (basket[basket.length - 1] === board[j][moves[i] - 1]) {
                          answer += 2;
                          board[j][moves[i] - 1] = 0
                          basket.pop();
                          break;
                      }
                  }
                  basket.push(board[j][moves[i] - 1]);
                  board[j][moves[i] - 1] = 0;
                  break;
              }
          }
      }
      return answer;
  }
  ```

  * 단순히 for문으로 문제에서 말하는대로 구현만 해주면 되는 문제였다.
  * 다른 사람의 풀이를 보며 다른 특별한 풀이법이 있을까 찾아보았지만 특별한 코드는 보이지 않았다.

## 두 개 뽑아서 더하기

* [문제 링크](https://programmers.co.kr/learn/courses/30/lessons/68644?language=javascript)

* 풀이

  ```js
  function solution(numbers) {
      var answer = [];
      numbers.sort()
      for (let i = 0; i < numbers.length; i++) {
          for (let j = i + 1; j < numbers.length; j++) {
              if (answer.find(item => item === numbers[i] + numbers[j]) === undefined) {
                  answer.push(numbers[i]+numbers[j])
              }
          }
      }
      answer.sort((a, b) => a - b)
      return answer;
  }
  ```

  * 이중 for문을 사용해 두 숫자를 뽑는 경우의 수를 모두 돌며 `answer` Array에 없는경우 추가해주었다.
  * `Set`을 사용하면 시간복잡도를 더 줄일 수 있겠지만, 경우의 수가 많지 않아 그냥 `find()` API를 써서 구현해주었다.

## 완주하지 못한 선수

* [문제 링크](https://programmers.co.kr/learn/courses/30/lessons/42576?language=javascript)

* 풀이

  ```js
  function solution(participant, completion) {
      const result = {};
      for (let i = 0; i < participant.length; i++) {
          if (!(participant[i] in result)) {
              result[participant[i]] = 0
          } else {
              result[participant[i]] += 1
          }
      }
      for (let i = 0; i < completion.length; i++) {
          if (result[completion[i]] === 0) {
              delete result[completion[i]]
          } else {
              result[completion[i]] -= 1
          }
      }
      return Object.keys(result)[0]
  }
  ```

  * `result` Object를 만들고 `participant`의 모든 값을 확인하며 key 값에 이름, value에 같은 이름이 나온 횟수를 저장하였다.
  * 마찬가지로 `completion`에서 for문을 돌며 value에 `-1`을 해주고 value가 0이 되면 Object에서 지워주어 마지막에 남는 이름을 출력해주었다.

* 다른 사람의 풀이(최인규 , 서경우 , 최민수 , charles2 님의 풀이)

  ```js
  var solution = (participant,completion) => participant.find(name=>!completion[name]--, completion.map(name=>completion[name]=(completion[name]|0)+1))
  ```

  * 먼저 `find(callback, thisArg)`의 `thisArg` 를 활용한 부분이 눈에 띈다. 

  * MDN을 참고해서 보니 `thisArg`는 `callback` 이 실행되기 전에 먼저 실행되는 `callback` function으로 내부에 `this`가 활용된다.

  * 따라서 `thisArg`에 해당하는 `completion.map()`이 먼저 실행이되고 내부를 살펴보면 `completion[name] = (completion[name] | 0) + 1`을 활용하여 `completion` Object의 key에 name, value에 갯수를 저장해준다.

    이때 if (!(name in completion))이 아닌 (completion[name] | 0)을 활용하여 없을 경우 한번에 `0`으로 만들어 주는 부분도 앞으로 활용도가 높을 것 같다.

  * `thisArg` 가 돌고 나서 `participant.find()` 함수가 동작한다. 이때 Arrow function을 활용하여 `!completion[name]--`를 사용해주었다. 이렇게 하면 `!completion[name]` 을 먼저 확인한 후 값을 1 감소시켜주어 `0`의 위치도 효과적으로 찾아줄 수 있다.

* 사실 문제의 풀이는 그렇게 까다롭지 않았지만 다른 사람의 풀이를 보며 많은 것을 배울 수 있는 좋은 문제였다.

## K번째수

* [문제 링크](https://programmers.co.kr/learn/courses/30/lessons/42748?language=javascript)

* 풀이

  ```js
  function solution(array, commands) {
    return commands.map((command) => {
      return array.slice(command[0] - 1, command[1]).sort((x, y) => x - y)[
        command[2] - 1
      ];
    });
  }
  ```

  * `Array.map()` 을 사용해서 command를 하나씩 받아오고 각 인덱스에 `i ~ j` 까지 슬라이스 한 Array를 sort한 후 k번째 수를 `return`하였다.
  * `sort()`를 사용할 때 그냥 해주면 사전순으로 정렬해주므로 `(x, y) => x - y`를 꼭 써야하는 것에 주의하자.

## 2016년

* [문제 링크](https://programmers.co.kr/learn/courses/30/lessons/12901?language=javascript)

* 풀이

  ```js
  function solution(a, b) {
      const days = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
      const months = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30]
      return days[(months.slice(0, a).reduce((x, y) => x + y, 0) + b) % 7];
  }
  ```

  * python에서 `sum()` 대신 js에는 `reduce()`를 사용한다.
  * `reduce(function, current value)`로 덧셈 말고도 원하는 연산을 수행할 수 있다.

## 3진법 뒤집기

* [문제 링크](https://programmers.co.kr/learn/courses/30/lessons/68935?language=javascript)

* 풀이

  ```js
  function solution(n) {
      let number = ''
      let answer = 0
      while (n > 0) {
          number = n % 3 + number;
          n = Math.floor(n / 3)
      }
      for (let i = 0; i < number.length; i++) {
          answer += number[i] * 3**i
      }
      return answer;
  }
  ```

  * 파이썬 같은 방식으로 풀었다.

  ```js
  // 다른 사람 풀이 soojeongHan , bangjaehun 님의 풀이
  const solution = (n) => {
      return parseInt([...n.toString(3)].reverse().join(""), 3);
  }
  ```

  * 다른사람의 풀이를 보다가 위와 같은 JavaScript다운 깔끔한 코드를 봤다. 

  * Spread syntax를 이용하여 Array에 넣어준다 이때 `numObj.toString([radix])`의 redix에 `2 ~ 36`의 숫자를 넣어주면 2진수에서 36진수까지 숫자를 변환하여 String으로 변환 해준다.

    [MDN toString()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/toString)

  * 이렇게 만든 Array를 `Array.reverse()`를 사용하여 뒤집어준다. 그 후 `Array.join("")`을 사용하여 다시 String으로 바꿔주고

  * `parseInt(string [, radix])` 를 사용하여 redix에 마찬가지로 `2 ~ 36` 진수 설정을 해줄 수 있다.

## 가운데 글자 가져오기

* [문제 링크](https://programmers.co.kr/learn/courses/30/lessons/12903?language=javascript)

* 풀이

  ```js
  function solution(s) {
    return s.length & 1
      ? s[Math.floor(s.length / 2)]
      : s[Math.floor(s.length / 2) - 1] + s[Math.floor(s.length / 2)];
  }
  ```

  * `조건 ? true : false `를 사용하여 풀어주었다.

## 같은 숫자는 싫어

* [문제 링크](https://programmers.co.kr/learn/courses/30/lessons/12906?language=javascript)

* 풀이

  ```js
  function solution(arr) {
      const answer = [];
      for  (let i = 0; i < arr.length; i++) {
          if (arr[i] != arr[i - 1]) {
              answer.push(arr[i]);
          }
      }
      return answer;
  }
  ```

  * 또 파이썬처럼 풀었다...

  ```js
  // 다른 사람의 풀이 jungting20 , - , 탈퇴한 사용자 , - , Junpil Hwang 외 116 명
  function solution(arr){
      return arr.filter((val,index) => val != arr[index+1]);
  }
  ```

  * 다른 사람의 풀이를 보니 `filter()`로 해결할 수 있는 문제였다. `Array.map()` 까지만 생각했었는데, 조건에 맞게 걸러줄 수 있는 `Array.filter()` 의 사용법을 알게된 좋은 문제였다.
  * 또한 `Array.filter()`는 조건이 `true`일 때 현재 값을 리턴해주므로 `return`이 아닌 조건을 넣어야 한다.

## 나누어 떨어지는 숫자 배열

* [문제 링크](https://programmers.co.kr/learn/courses/30/lessons/12910?language=javascript)

* 풀이

  ```js
  function solution(arr, divisor) {
      const result = arr.filter(num => num%divisor == 0);
      return result.length > 0 ? result.sort((x, y) => x - y) : [-1];
  }
  ```

  * 위의 문제 처럼 `Array.filter()`를 사용하면 풀 수 있는 문제였다.
  * 예외 처리를 해주어야 해서 `result`에 값이 들어있는지 확인하는 삼항 연산자(Conditional Ternary Operator)`조건 ? true : false` 를 사용해주었다.

## 두 정수 사이의 합

* [문제 링크](https://programmers.co.kr/learn/courses/30/lessons/12912)

* 풀이

  ```js
  function solution(a, b) {
      return a > b ? (a + b) * (a - b + 1) / 2 : (a + b) * (b - a + 1) / 2;
  }
  ```

  * 삼항 연산자를 이용해서 풀어주었다.

  ```js
  // 다른 사람의 풀이 박홍철 님의 풀이
  function adder(a, b){
      return (a+b)*(Math.abs(b-a)+1)/2;
  }
  ```

  * 다른 사람의 풀이도 살펴보았는데 이 풀이법이 좀 더 깔끔한 것 같다.

## 문자열 내 마음대로 정렬하기

* [문제 링크](https://programmers.co.kr/learn/courses/30/lessons/12915)

* 풀이

  ```js
  function solution(strings, n) {
      return strings.sort((x, y) => {
          return x[n] > y[n] ? 1 : x[n] === y[n] ? x > y ? 1 : -1
      });
  }
  ```

  * 삼항연산자를 세번 써주어서 해결하였다.
  * 삼항연산자를 중복으로 써주어서 가독성이 떨어져 좋은 코드는 아닌 것 같다.

  ```js
  // 다른 사람의 풀이 - , kimdongwon , 호리 , 날코딩 , 이석원 외 11 명
  function solution(strings, n) {
      return strings.sort((s1, s2) => s1[n] === s2[n] ? s1.localeCompare(s2) : s1[n].localeCompare(s2[n]));
  }
  ```

  * 다른 사람의 풀이를 보자 `String.localeCompare(비교할 문자)` 를 사용하여 한번에 비교를 해주었다.
  * [MDN String.localeCompare()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/localeCompare)

## 문자열 내 p와 y의 개수

* [문제 링크](https://programmers.co.kr/learn/courses/30/lessons/12916?language=javascript)

* 풀이

  ```js
  function solution(s){
      let cntP = 0
      let cntY = 0
      for (let i = 0; i < s.length; i++) {
          if (s[i] === 'p' | s[i] === 'P') cntP++
          else if (s[i] === 'y' | s[i] === 'Y') cntY++
      }
      return cntP == cntY ? true : false;
  }
  ```

  * 그냥 반복문을 돌며 count 해주었다.

  ```js
  // 다른 사람의 풀이 temp , - , - , - , - 외 23 명
  function solution(s) {
    return s.match(/p/gi).length == s.match(/y/gi).length;
  }
  ```

  * `String.match()`를 사용하여 간단하게 해결할 수 있었다.
  * `/문자/` 를 통해 찾고 싶은 문자를 찾는다 이때 첫번째 문자를 찾으면 바로 리턴해주는데 모든 문자를 찾기위해 `g` flag를 붙여준다.
  * 이번에는 대문자와 소문자를 다른 문자로 판단해 제대로 값이 나오지 않는다 `i` flag를 붙여주면 대소문자를 구분하지 않는다.
  * `ig`와 `gi` 모두 사용할 수 있지만 보통 gi로 사용하는 것 같다.
  * [MDN String.match()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/match)

## 문자열 내림차순으로 배치하기

* [문제 링크](https://programmers.co.kr/learn/courses/30/lessons/12917?language=javascript)

* 풀이

  ```js
  function solution(s) {
      return [...s].sort((x, y) => x > y ? -1 : 1).join('');
  }
  ```

  * Spread syntax(...)을 이용하여 String을 Array로 바꿔준다.
  * 이후 sort를 사용하여 `x > y` 일 경우 `-1`을 줘서 사전 역순으로 정렬한다.
  * `Array.join()`을 써서 다시 문자열로 바꿔준다.

## 문자열 다루기 기본

* [문제 링크](https://programmers.co.kr/learn/courses/30/lessons/12918?language=javascript)

* 풀이

  ```js
  function solution(s) {
      const number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
      if (s.length !== 4 & s.length !== 6) {
          return false;
      }
      for (let i = 0; i < s.length; i++) {
          if (!(s[i] in number)) {
              return false;
          }
      }
      return true;
  }
  ```

  * 길이 조건을 만족 하지 못할 경우 한번 걸러주고
  * `number` Array를 만들어서 `number`에 없는 문자가 있을 경우 `false`를, 모두 통과했을 때는 `true`를 리턴하였다.

  ```js
  // 다른 사람의 풀이 다들 탈퇴해서 ID가 안보임...
  function alpha_string46(s){
    var regex = /^\d{6}$|^\d{4}$/;
    return regex.test(s);
  }
  ```

  * 정규 표현식을 활용한 풀이이다.
  * [MDN 정규식](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/%EC%A0%95%EA%B7%9C%EC%8B%9D)
  * `/ /` 정규식 리터럴(슬래쉬`/`로 감싸는 패턴)을 사용하면 정규식을 만들 수 있다.
  * `^` : 입력의 시작부분 문자셋 `[^xyz]`와 혼동하지 않게 조심하자.
  * `$` : 입력의 끝부분
  * `\d` : 숫자에 대응 [0 - 9]
  * `{n}` : 앞 표현식을 `n`번 나타낸다.
  * `x|y` : or
  * `정규식.test(String)` 정규식에 대응되는지 검사하는 메소드 

## 서울에서 김서방 찾기

* [문제 링크](https://programmers.co.kr/learn/courses/30/lessons/12919?language=javascript)

* 풀이

  ```js
  function solution(seoul) {
      return `김서방은 ${seoul.indexOf("Kim")}에 있다`;
  }
  ```

  * 템플릿 리터럴(Template literals)을 사용하면 간단하게 풀 수 있다.
  * [MDN Template literals](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Template_literals)
  * `"Kim"`의 index는 `Array.indexOf("Kim")` 으로 찾을 수 있다.

## 수박수박수박수박수박수?

* [문제 링크](https://programmers.co.kr/learn/courses/30/lessons/12922?language=javascript)

* 풀이

  ```js
  function solution(n) {
      var answer = '';
      for (let i = 0; i < n; i++) {
          if (i & 1) {
              answer += '박';
          } else {
              answer += '수';
          }
      }
      return answer;
  }
  ```

  * n번 반복문을 돌며 짝수 자리에는 `박`, 홀수 자리에는 `수`가 오도록 하였다.
  * 하지만 메모리 공간을 `n`개 만큼 차지하여 좋은 코드는 아닌것 같다

  ```js
  // 다른 사람의 풀이 이수관 님의 풀이
  const waterMelon = n => {
      return '수박'.repeat(n/2) + (n%2 === 1 ? '수' : '');
  }
  ```

  * 다른 사람의 풀이를 보자 `String.repeat()` method를 사용하여 해결한 풀이법을 보았다.
  * `String.repeat(count)` method는 String을 글자 하나하나씩 나눠 Array로 변환해 준 후 count(소수점 뒤는 버림) 만큼 반복해서 `push`해주고 마지막으로 다시 String으로 변환시키는 방식으로 동작 한다.
  * 자세한 설명 [Implementing JDK String.repeat in Java 11](https://medium.com/@ggajos/java-11-how-string-repeat-was-implemented-and-why-d93796b7abba)
  * 따라서 메모리 공간에 Array를 저장하는 공간, `수`와 `박` String을 저장하는 공간만 필요하므로 위의 코드보다 훨씬 효율적이다.

## 문자열을 정수로 바꾸기

* [문제 링크](https://programmers.co.kr/learn/courses/30/lessons/12925?language=javascript)

* 풀이

  ```js
  function solution(s) {
      return parseInt(s);
  }
  ```

  * parseInt를 사용하면 문자열을 숫자로 바꿔준다.

  * `String` 과 `Number`의 사칙연산을 수행하면 `Number`로 나오는 특성을 이용해서 푼 사람들도 많았다.

    하지만 그러한 풀이법은 명시적이지 못해 이렇게 명시적으로 표현해 주는 것이 더 좋은 풀이법이다.

## 내적

* [문제 링크](https://programmers.co.kr/learn/courses/30/lessons/70128?language=javascript)

* 풀이

  ```js
  function solution(a, b) {
      let answer = 0;
      for (let i = 0; i < a.length; i++) {
          answer += a[i] * b[i]
      }
      return answer;
  }
  ```

  * 반복문을 돌며 같은 인덱스의 숫자를 곱해 answer에 더해주었다.

  ```js
  // 다른 사람의 풀이 고우혁님의 풀이
  function solution(a, b) {
      return a.reduce((acc, _, i) => acc += a[i] * b[i], 0);
  }
  ```

  * 다른 사람의 풀이를 보자
  * `arr.reduce(callback( accumulator, currentValue, [, index[, array]] )[, initialValue])`를 사용하여 인덱스도 받아 올 수 있다.
  * 이를 통해 `b`에서 같은 인덱스의 값을 곱해주어 간단하게 해결 할 수 있다.

## 시저 암호

* [문제 링크](https://programmers.co.kr/learn/courses/30/lessons/12926)

* 풀이

  ```js
  function solution(s, n) {
      const answer = [];
      for (let i = 0; i < s.length; i++) {
          if (s[i] !== ' ') {
              const word = s.charCodeAt(i);
              if (word >= 65 & word <= 90) {
                  answer.push(String.fromCharCode(word + n > 90 ? word + n - 26 : word + n))
              } else {
                  answer.push(String.fromCharCode(word + n > 122 ? word + n - 26 : word + n))
              }
          } else {
              answer.push(' ')
          }
      }
      return answer.join('');
  }
  ```

  * ascii code를 활용하여 풀었다.

  ```js
  // 다른 사람의 풀이 쿠키님의 풀이
  function solution(s, n) {
      var upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
      var lower = "abcdefghijklmnopqrstuvwxyz";
      var answer= '';
  
      for(var i =0; i <s.length; i++){
          var text = s[i];
          if(text == ' ') {
              answer += ' '; 
              continue;
          }
          var textArr = upper.includes(text) ? upper : lower;
          var index = textArr.indexOf(text)+n;
          if(index >= textArr.length) index -= textArr.length;
          answer += textArr[index];
      }
      return answer;
  }
  ```

  * 대소문자와 공백만 있으므로 Alphabet String을 모두 만들어 주고 `String.includes()`를 활용하여 푼 코드다.
  * 이 방법도 깔끔하고 괜찮은 것 같다.

## 약수의 합

* [문제 링크](https://programmers.co.kr/learn/courses/30/lessons/12928)

* 풀이

  ```js
  function solution(n) {
    let answer = 0;
    for (let i = 1; i <= n ** 0.5; i++) {
      if (!(n % i)) {
        if (i == n ** 0.5) {
          answer += i;
        } else {
          answer += i + n / i;
        }
      }
    }
    return answer;
  }
  ```

  * 루트 n 까지의 숫자 중 n의 약수를 찾아 그 숫자와 나누었을 때 몫을 answer에 더해주었다.
  * 간단한 방법이 있을지 다른 사람의 코드를 보았지만 모두 비효율적이라 따로 배울만한 것은 없었다.

## 이상한 문자 만들기

* [문제 링크](https://programmers.co.kr/learn/courses/30/lessons/12930?language=javascript)

* 풀이

  ```js
  function solution(s) {
      var answer = [];
      let cnt = 0
      for (let i = 0; i < s.length; i++) {
          if (s[i] !== ' ') {
              if (cnt === 0) {
                  answer.push(s[i].toUpperCase());
                  cnt = 1
              } else {
                  answer.push(s[i].toLowerCase());
                  cnt = 0
              }
          } else {
              answer.push(s[i]);
              cnt = 0
          }
      }
      return answer.join('');
  }
  ```

  * 메모리 사용량을 줄이기 위해 answer를 Array로 바꿔주고 for문을 돌며 대소문자를 바꿔주었다.

  ```js
  // 다른 사람의 풀이 탈퇴한 사람의 풀이
  function solution(s) {
    function change(a) {
      return a[0].toUpperCase() + a[1].toLowerCase();
    }
    return s.toUpperCase().replace(/(\w)(\w)/g, change);
  }
  ```

  * 효율성은 떨어지지만 정규표현식을 사용한 재밌는 풀이법이 있었다.

  ```js
  // 다른 사람의 풀이 ._.님의 풀이
  function solution(s) {
    return s.split(' ').map((a) => {
      return a.split('').map((b, i) => {
        return (i % 2 === 0) ? b.toUpperCase() : b.toLowerCase();
      }).join('');
    }).join(' ');
  }
  ```

  * 위의 내 풀이방법을 `map()`과 `split()`, `join()`을 사용하면 훨씬 간단하게 표현할 수 있다.
  * `map()` 활용에 좀 더 신경써야겠다.

## 자릿수 더하기

* [문제 링크](https://programmers.co.kr/learn/courses/30/lessons/12931?language=javascript)

* 풀이

  ```js
  function solution(n) {
      return n.toString().split('').reduce((x, y) => x += parseInt(y), 0);
  }
  ```

  * Number를 String으로 바꿔준 후 `split()`으로 나눠 Array로 만들어주고 `reduce()`를 활용하여 각 자리 수 를 모두 더해주었다.

## 자연수 뒤집어 배열로 만들기

* [문제 링크](https://programmers.co.kr/learn/courses/30/lessons/12932?language=javascript)

* 풀이

  ```js
  function solution(n) {
      return n.toString().split('').reverse().map(num => parseInt(num));
  }
  ```

  * `toString()`을 사용하여 String으로 바꿔준 후 한 글자씩 나눠 `reverse()` 후 Number로 다시 바꿔주었다.

## 정수 내림차순으로 배치하기

* [문제 링크](https://programmers.co.kr/learn/courses/30/lessons/12933?language=javascript)

* 풀이

  ```js
  function solution(n) {
      return parseInt(n.toString().split('').sort((x, y) => parseInt(y) - parseInt(x)).join(''));
  }
  ```

  * n을 문자열로 바꿔준 후 `split()`으로 Array로 바꿔준 후 내림차순으로 정렬하고 `join()`을 통해 String 다시 변환 후 `parseInt()`를 써서 Number로 바꿔주었다.

## 정수 제곱근 판별

* [문제 링크](https://programmers.co.kr/learn/courses/30/lessons/12934?language=javascript)

* 풀이

  ```js
  function solution(n) {
      return Math.sqrt(n) % 1 ? -1 : (Math.sqrt(n) + 1)**2;
  }
  ```

  * n의 제곱근에 소수점 뒷자리수가 있으면 `-1` 없으면 `(제곱근 + 1)의 제곱`을 리턴하였다.

## 제일 작은 수 제거하기

* [문제 링크](https://programmers.co.kr/learn/courses/30/lessons/12935)

* 풀이

  ```js
  function solution(arr) {
    return arr.length > 1 ? arr.filter((num) => num !== Math.min(...arr)) : [-1];
  }
  ```

  * `filter()`로 한번에 해결할 수 있지 않을까 생각했는데 실행시간이 엄청 오래걸렸다.
  * 매번 `Math.min(...arr)`을 계산해서 그런 것 같아 `minNum` 변수를 따로 만들어주고 실행 시켜보았지만 그래도 아래의 코드보다 훨씬 오래걸렸다.

  ```js
  // 다른 사람의 풀이 lsw015 , developer-do , 노국현 , - , 정만수님 외 9 명
  function solution(arr) {
      arr.splice(arr.indexOf(Math.min(...arr)), 1)
      return arr.length > 0 ? arr : [-1];
  }
  ```

  * `Array.splice()`를 통해 Array 원하는 부분을 잘라낼 수 있다.
  * 새로운 method를 알게 되었다.

## 짝수와 홀수

* [문제 링크](https://programmers.co.kr/learn/courses/30/lessons/12937?language=javascript)

* 풀이

  ```js
  function solution(num) {
    return num & 1 ? "Odd" : "Even";
  }
  ```

  * 비트연산자를 활용해 홀수인지 확인해주었다.

## 콜라츠 추측

* [문제 링크](https://programmers.co.kr/learn/courses/30/lessons/12943?language=javascript)

* 풀이

  ```js
  function solution(num) {
      for (let i = 0; i < 501; i++) {
          if (num === 1) {
              return i
          } else {
              num & 1 ? num = num * 3 + 1 : num /= 2;
          }
      }
      return -1;
  }
  ```

  * for문을 통해 501번 반복문을 실행시켜주고
  * for문 안에 return을 사용해주기 위해 if문을 사용해주었다.
  * 홀수 짝수 구분에는 삼항연산자를 이용해주었다.

## 평균 구하기

* [문제 링크](https://programmers.co.kr/learn/courses/30/lessons/12944?language=javascript)

* 풀이

  ```js
  function solution(arr) {
      return arr.reduce((x, y) => x += y / arr.length, 0)
  }
  ```

  * `Array.reduce()`를 활용하면 간단하게 해결할 수 있다.

## 하샤드 수

* [문제 링크](https://programmers.co.kr/learn/courses/30/lessons/12947?language=javascript)

* 풀이

  ```js
  function solution(x) {
      return x % x.toString().split('').reduce((x, y) => x += parseInt(y), 0) == 0;
  }
  ```

  * `Number.toString()`, `String.split()`, `Array.reduce()` 를 활용하여 한줄로 풀어보았다.
  * 하지만 입력 데이터의 크기가 커지면 `Number`에서 바로 처리하는 것이 훨씬 빠르므로 for문을 사용하자

## 핸드폰 번호 가리기

* [문제 링크](https://programmers.co.kr/learn/courses/30/lessons/12948?language=javascript)

* 풀이

  ```js
  function solution(phone_number) {
      return phone_number.split('').reduce((x, y, idx) => x += idx < phone_number.length - 4 ? '*' : y, '');
  }
  
  function solution(phone_number) {
      return phone_number.split('').map((num, idx) => idx < phone_number.length - 4 ? '*' : num).join('');
  }
  ```

  * `Array.reduce()`, `Array.map()`을 활용한 두가지 방법으로 해결해보았다. `reduce()`를 사용할 경우 데이터 메모리 공간을 더 많이 사용하므로 `map()`으로 해결하는 것이 효율성이 더 좋다.

## 행렬의 덧셈

* [문제 링크](https://programmers.co.kr/learn/courses/30/lessons/12950?language=javascript)

* 풀이

  ```js
  function solution(arr1, arr2) {
      return arr1.map((arr, i) => arr.map((a, j) => a + arr2[i][j]));
  }
  ```

  * `Array.map()`을 이중으로 사용하여 간단하게 해결해보았다.

## x만큼 간격이 있는 n개의 숫자

* [문제 링크]

* 풀이

  ```js
  function solution(x, n) {
      let answer = [];
      for (let i = 1; i <= n; i++) {
          answer.push(x*i)
      }
      return answer;
  }
  ```

  * for문과 `Array.push()`를 활용하여 풀어보았다.
  * 하지만 다른 더욱 간단한 코드가 있을 것 같아 다른 사람의 코드를 보니 아래와 같은 코드가 있었다.

  ```js
  function solution(x, n) {
    return [...Array(n)].map((v, idx) => (idx + 1) * x);
  }
  ```

  * `Array(n)`을 써서 n개의 Array를 만들어주고 `Array.map()`을 사용하면 훨씬 간단한 코드가 나온다. 

## 직사각형 별찍기

* [문제 링크](https://programmers.co.kr/learn/courses/30/lessons/12969?language=javascript)

* 풀이

  ```js
  process.stdin.setEncoding('utf8');
  process.stdin.on('data', data => {
      const n = data.split(" ");
      const a = Number(n[0]), b = Number(n[1]);
      for (let i = 0; i < b; i++) {
          console.log('*'.repeat(a))
      }
  });
  ```

  * `String.repeat(count)`를 사용하여 문자열을 count만큼 반복해서 이어 붙일 수 있다.