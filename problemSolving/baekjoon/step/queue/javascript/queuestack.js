const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n")
  .map((line) => line.split(" ").map(Number));

const N = input[0][0];
const queuestack = input[1];
const stack = input[2];
const M = input[3][0];
const request = input[4];

function solution(n, queue, stack, m, req) {
  const answer = [];
  let index = N - 1;

  for (let i = 0; i < m; i++) {
    while (queue[index]) {
      index--;
    }

    if (index < 0) {
      break;
    }

    answer.push(stack[index]);
    index--;
  }

  if (answer.length < m) {
    const remaining = m - answer.length;
    for (let i = 0; i < remaining; i++) {
      answer.push(req[i]);
    }
  }

  return answer.join(' ');
}
console.log(solution(N, queuestack, stack, M, request));