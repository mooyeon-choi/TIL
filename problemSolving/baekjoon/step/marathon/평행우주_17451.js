const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n")
  .map((str) => str.split(" ").map(Number));

const N = input[0][0];
const ARR = input[1];

function solution(n, arr) {
  let answer = 0;
  for (let i = n - 1; i >= 0; i--) {
    if (arr[i] > answer) {
      answer = arr[i];
    } else {
      answer = arr[i] * Math.ceil(answer / arr[i]);
    }
  }

  return answer;
}

console.log(solution(N, ARR));