const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n");

const N = Number(input[0]);
const arr = input[1].split(" ").map(Number).sort((a, b) => a - b);
const X = Number(input[2]);

function solution() {
  let left = 0;
  let right = N - 1;
  let cnt = 0;

  while (left < right) {
    const sum = arr[left] + arr[right];
    if (sum === X) {
      left++;
      right--;
      cnt++;
    } else if (sum < X) {
      left++;
    } else {
      right--;
    }
  }

  return cnt;
}

console.log(solution());
