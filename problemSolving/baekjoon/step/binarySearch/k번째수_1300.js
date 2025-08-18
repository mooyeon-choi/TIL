const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n")
  .map(Number);

const N = input[0];
const K = input[1];

function solution() {
  let left = 1;
  let right = N ** 2;

  while (left <= right) {
    const mid = Math.floor((left + right) / 2);
    let count = 0;

    for (let i = 1; i <= N; i++) {
      count += Math.min(Math.floor(mid / i), N);
    }

    if (count < K) {
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }
  return left;
}

console.log(solution());