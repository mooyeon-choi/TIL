# Level 1 (JavaScript)

## 목차

* [기능개발](#기능개발)
* [타겟 넘버](#타겟-넘버)
* [카펫](#카펫)
* [다음 큰 숫자](#다음-큰-숫자)
* [폰켓몬](#폰켓몬)
* [n진수 게임](#n진수-게임)

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

## 타겟 넘버

* [문제 링크](https://programmers.co.kr/learn/courses/30/lessons/43165?language=javascript)

* 풀이

  ```js
  function solution(numbers, target) {
    let answer = 0;
    dfs(0, 0);
    function dfs(num, index) {
      if (index < numbers.length) {
        dfs(num + numbers[index], index + 1);
        dfs(num - numbers[index], index + 1);
      } else {
        if (num === target) {
          answer++;
        }
      }
    }
    return answer;
  }
  ```

  * DFS 완전탐색을 통해 풀 수 있는 문제였다.

## 카펫

* [문제 링크](https://programmers.co.kr/learn/courses/30/lessons/42842?language=javascript)

* 풀이

  ```js
  function solution(brown, yellow) {
      for (let i = (brown + 4) / 2 - 3; i >= (brown + 4) / 4; i--) {
          if (i * ((brown + 4) / 2 - i) === brown + yellow) {
              return [i, (brown + 4) / 2 - i]
          }
      }
  }
  ```

  * 수학적으로 접근하면 어렵지않게 해결할 수 있는 문제였다.
  * 한변의 길이는 반드시 3보다

## 다음 큰 숫자

* [문제 링크](https://programmers.co.kr/learn/courses/30/lessons/12911?language=javascript)

* 풀이

  ```js
  function solution(n) {
      const cnt = n.toString(2).match(/[1]/g).length;
      while (true) {
          n++
          if (n.toString(2).match(/[1]/g).length === cnt) {
              return n
          }
      }
  }
  ```

  * 정규 표현식과 `number.toString()`을 활용하면 간단하게 풀 수 있다.
  * 하지만 숫자가 아주 클 경우 다른 공식을 찾아서 해결해야할 것 같다.

## 폰켓몬

* [문제 링크](https://programmers.co.kr/learn/courses/30/lessons/1845?language=javascript)

* 풀이

  ```js
  function solution(nums) {
      const answer = new Set(nums);
      return answer.size <= nums.length / 2 ? answer.size : nums.length / 2;
  }
  ```

  * Set과 삼항 연산자로 간단하게 해결할 수 있다.

## n진수 게임

* [문제 링크](https://programmers.co.kr/learn/courses/30/lessons/17687?language=javascript#)

* 풀이

  ```js
  function solution(n, t, m, p) {
      const result = [];
      let answer = '';
      let num = 0;
      while (result.length < t * m) {
          result.push(...num.toString(n).toUpperCase().split(''));
          num++
      }
      for (let i = p - 1; i < result.length; i += m) {
          answer += result[i]
          if (answer.length === t) break;
      }
      return answer;
  }
  ```

  * `t * m` 길이의 `Array`를 만들어준 후 `p - 1` 에서 `m` 씩 증가하는 인덱스에 위치한 문자를 더해주는 방식으로 해결하였다.