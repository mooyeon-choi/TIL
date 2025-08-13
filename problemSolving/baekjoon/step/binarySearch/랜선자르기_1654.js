const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n");

const [K, N] = input[0].split(" ").map(Number);
const lengths = input.slice(1).map(Number);

function solution(arr, target) {
  let left = 1;
  let right = Math.max(...arr);

  while (left <= right) {
    const mid = Math.floor((left + right) / 2);
    const count = arr.reduce((sum, length) => sum + Math.floor(length / mid), 0);

    if (count < target) {
      right = mid - 1;
    } else {
      left = mid + 1;
    }
  }
  return left - 1;
}

console.log(solution(lengths, N));