const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n");

const N = Number(input[0]);
const A = input[1].split(" ").map(Number).sort((a, b) => a - b);
const M = Number(input[2]);
const targets = input[3].split(" ").map(Number);

function binarySearch(arr, target) {
  let left = 0;
  let right = arr.length - 1;

  while (left <= right) {
    const mid = Math.floor((left + right) / 2);
    if (arr[mid] === target) {
      return 1;
    } else if (arr[mid] < target) {
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }
  return 0;
}

function solution() {
  const result = [];

  for (const target of targets) {
    const found = binarySearch(A, target);

    result.push(found ? 1 : 0);
  }

  return result.join("\n");
}

console.log(solution(N, A, M, targets));