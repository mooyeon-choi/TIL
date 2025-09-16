const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n");

const [N, S] = input[0].split(" ").map(Number);
const arr = input[1].split(" ").map(Number);

function solution() {
  let left = 0;
  let right = 0;
  let sum = 0;
  let minLength = Infinity;

  while (right < N) {
    sum += arr[right];
    right++;

    while (sum >= S && left < right) {
      minLength = Math.min(minLength, right - left);
      sum -= arr[left];
      left++;
    }
  }

  return minLength === Infinity ? 0 : minLength;
}

console.log(solution());
