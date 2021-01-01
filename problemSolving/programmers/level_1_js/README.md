# Level 1 (JavaScript)

## 목차

* [크레인 인형뽑기 게임](#크레인-인형뽑기-게임)
* [두 개 뽑아서 더하기](#두-개-뽑아서-더하기)
* [완주하지 못한 선수](#완주하지-못한-선수)
* [K번째수](#k번째수)
* [2016년](2016년)
* [3진법 뒤집기](#3진법-뒤집기)

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