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
