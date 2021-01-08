# Level 1 (JavaScript)

## 목차

* [기능개발](#기능개발)

## 기능개발

* [문제 링크](https://programmers.co.kr/learn/courses/30/lessons/42586?language=javascript)

* 풀이

  ```js
  function solution(progresses, speeds) {
      const answer = [];
      let time = 1;
      let cnt = 0;
      for (let i = 0; i < progresses.length; i++) {
          if (progresses[i] + speeds[i] * time < 100) {
              i !== 0 && answer.push(cnt)
              time = Math.ceil((100 - progresses[i]) / speeds[i]);
              cnt = 1
          } else {
              cnt += 1
          }
      }
      answer.push(cnt)
      return answer;
  }
  ```

  * 문제 분류는 큐/스택으로 되어있지만 반복문을 통해 해결하는 것이 더 효율성이 좋을 것 같아 반복문을 통해 풀어주었다.