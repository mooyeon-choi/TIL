# Level 3 (JavaScript)

## 목차

* [정수 삼각형](#정수-삼각형)

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