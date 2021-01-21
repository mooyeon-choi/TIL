# Level 3 (JavaScript)

## 목차

* [단속 카메라](#단속-카메라)
* [정수 삼각형](#정수-삼각형)

## 단속 카메라

* [문제 링크](https://programmers.co.kr/learn/courses/30/lessons/42884?language=javascript)

* 풀이

  ```js
  function solution(routes) {
      let answer = 0;
      routes.sort((x, y) => x[0] - y[0]);
      let maxnum = routes[0][1]
      for (let i = 0; i < routes.length; i++) {
          if (maxnum >= routes[i][0]) {
              if (maxnum > routes[i][1]) {
                  maxnum = routes[i][1];
              }
          } else {
              answer++;
              maxnum = routes[i][1]
          }
      }
      return answer + 1;
  }
  ```

  * 정렬을 사용해 풀어주면 간단하게 해결 할 수 있다. 

## 정수 삼각형

* [문제 링크](https://programmers.co.kr/learn/courses/30/lessons/43105?language=javascript)

* 풀이

  ```js
  function solution(triangle) {
      for (let i = triangle.length - 2; i > -1; i--) {
          for (let j = 0; j < triangle.length; j++) {
              triangle[i][j] += Math.max(triangle[i + 1][j], triangle[i + 1][j + 1])
          }
      }
      return triangle[0][0];
  }
  ```

  * Bottom에서 top으로 거꾸로 확인하며 DP를 활용하여 풀면 간단하게 해결되는 문제였다.
  * 바로 다음 인덱스의 `j`, `j+1` 번째 위치의 숫자 중 큰 값을 계속 더해주며 `[0][0]` 위치까지 올라가면 시간복잡도 `O(n)`으로 답을 찾을 수 있다.