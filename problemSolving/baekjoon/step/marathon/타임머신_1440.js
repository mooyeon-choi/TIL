const input = require('fs').readFileSync('/dev/stdin').toString().trim().split(':');

function solution(input) {
  let answer = 0;

  for (let i = 0; i < input.length; i++) {
    const num = Number(input[i]);

    if (num >= 60) {
      return 0;
    }
  }
 
  for (let i = 0; i < input.length; i++) {
    const num = Number(input[i]);

    if (num > 0 && num <= 12) {
      answer += 2;
    }
  }

  return answer;
}

console.log(solution(input));