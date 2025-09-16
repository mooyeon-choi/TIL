const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n")
  .map((line) => line.split(" ").map(Number));

const N = input[0][0];
const items = input[1].sort((a, b) => a - b);

function solution() {
  let left = 0;
  let right = items.length - 1;
  let answer = [0, 0];
  let minDiff = Infinity;

  while (left < right) {
    const sum = items[left] + items[right];
    const diff = Math.abs(sum);

    if (diff < minDiff) {
      minDiff = diff;
      answer = [items[left], items[right]];
    }

    if (sum < 0) {
      left++;
    } else {
      right--;
    }
  }

  return answer;
}

console.log(solution().join(" "));
