const input = require('fs').readFileSync('/dev/stdin').toString().trim();

const num = Number(input);

function solution(n) {
  if (n >= 199) return 0;
  return 199 - n;
}

console.log(solution(num));