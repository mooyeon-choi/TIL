const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n")
  .map((line) => line.split(" ").map(Number));

const N = input[0][0];
const request = input[1];

function solution(n, req) {
  const deque = [];
  for (let i = 0; i < n; i++) {
    deque.push({ index: i + 1, value: req[i] });
  }
  const answer = [];
  let idx = 0;

  while (deque.length > 0) {
    const { index, value } = deque.splice(idx, 1)[0];
    answer.push(index);
    if (deque.length === 0) break;
    if (value > 0) {
      idx = (idx + value - 1) % deque.length;
    } else {
      idx = (idx + value + deque.length) % deque.length;
    }
  }
  return answer.join(' ');
}

console.log(solution(N, request));