const input = require('fs').readFileSync('/dev/stdin').toString().trim();

function solution(input) {
  if (input.length % 2 === 1) {
    return "fix";
  }

  return input.indexOf(")") === input.length / 2 ? "correct" : "fix";
}

console.log(solution(input));