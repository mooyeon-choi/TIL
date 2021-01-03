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
