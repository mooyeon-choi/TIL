const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n")
  .map((str) => str.split(" ").map(Number));

const N = input[0][0];
const ARR = input.slice(1);

function solution(n, arr) {
  let minNum = 0;
  let maxNum = 0;

  for (let i = 0; i < n; i++) {
    if (Math.min(...arr[i]) > minNum) minNum = Math.min(...arr[i]);
    if (Math.max(...arr[i]) > maxNum) maxNum = Math.max(...arr[i]);
  }

  minNum = BigInt(minNum);
  maxNum = BigInt(maxNum);
  return (minNum * maxNum).toString();
}

console.log(solution(N, ARR));