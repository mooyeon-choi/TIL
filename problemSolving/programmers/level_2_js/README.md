# Level 2 (JavaScript)

## 목차

* [스킬트리](#스킬트리)
* [기능개발](#기능개발)
* [H-Index](#h-index)
* [타겟 넘버](#타겟-넘버)
* [카펫](#카펫)
* [다음 큰 숫자](#다음-큰-숫자)
* [폰켓몬](#폰켓몬)
* [이진 변환 반복하기](#이진-변환-반복하기)
* [n진수 게임](#n진수-게임)

## 스킬트리

* [문제 링크](https://programmers.co.kr/learn/courses/30/lessons/49993?language=javascript)

* 풀이

  ```js
  function solution(skill, skill_trees) {
      var answer = 0;
      let before;
      let check;
      for (let i = 0; i < skill_trees.length; i++) {
          before = -1;
          check = true;
          for (let j = 0; j < skill.length; j++) {
              if (skill_trees[i].indexOf(skill[j]) !== -1) {
                  if (skill_trees[i].indexOf(skill[j]) > before) {
                      before = skill_trees[i].indexOf(skill[j]);
                  } else {
                      check = false;
                      break;
                  }
              } else {
                  before = 27;
              }
          }
          answer += check ? 1 : 0
      }
      return answer;
  }
  
  // 다른 사람의 풀이 iRequestUResponse , milliwonaire , 박하영님의 풀이
  function solution(skill, skill_trees) {
      function isCorrect(n) {
          let test = skill.split('');
          for (var i = 0; i < n.length; i++) {
              if (!skill.includes(n[i])) continue;
              if (n[i] === test.shift()) continue;
              return false;
          }
          return true;
      }    
  
      return skill_trees.filter(isCorrect).length;
  }
  ```

  * 2중 for문을 사용해서 풀어주었다.
  * `skill_tree`의 최대 크기가 `26`이므로 없는 값의 경우 `27`을 넣어주고 이전 스킬의 `index`가 항상 더 작을때만 `check`가 `true`값이 나와 `answer`에 1을 더해주도록 해주었다.
  * 다른 사람의 풀이를 보자 중복되는 스킬이 없다는 점을 이용하여 `isCorrect` 함수로 훨씬 간단하게 구현한 것을 보았다.
  * `skill_tree`를 하나씩 확인하며 해당 인덱스의 문자가 skill에 없다면 `continue`, `skill`에 있지만 `skill`의 가장 앞에 없는 경우 문제 조건에 걸리므로 `false`를 리턴하도록 하여 간단하게 풀 수 있다.

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

## H-Index

* [문제 링크](https://programmers.co.kr/learn/courses/30/lessons/42747?language=javascript)

* 풀이

  ```js
  function solution(citations) {
      citations.sort((x, y) => y - x);
      for (let i = 0; i < citations.length; i++) {
          if (citations[i] < i + 1) {
              return i;
          }
      }
      return citations.length;
  }
  ```

  * 정렬을 통해 간단하게 해결할 수 있다.
  * h이상인 수가 h이상 있는 최대값이 H-Index이므로 `큰 수 -> 작은 수`로 정렬해주고 `index + 1` 보다 현재 값이 작을 때 `index`를 리턴해준다.
  * 값이 모두 Array의 크기보다 클 경우 Array의 길이를 리턴해준다.

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

## 이진 변환 반복하기

* [문제 링크](https://programmers.co.kr/learn/courses/30/lessons/70129?language=javascript)

* 풀이

  ```js
  function solution(s) {
      const answer = [0, 0];
      while (s.length > 1) {
          answer[0]++;
          answer[1] += s.match(/[0]/g) ? s.match(/[0]/g).length : 0;
          s = s.split('0').join('').length.toString(2);
      }
      return answer;
  }
  ```

  * 정규표현식을 통해 String에서 `0`의 갯수를 구하고
  * `0`을 지워준 후 String의 길이를 다시 이진수로 변환하여 다음 수를 찾아주었다.

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
