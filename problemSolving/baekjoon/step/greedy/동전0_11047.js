const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n");

const [N, K] = input[0].split(" ").map(Number);
const coins = input.slice(1).map(Number);

function solution() {
  let change = K;
  let answer = 0;
  for (let i = N - 1; i >= 0; i--) {
    if (change === 0) break;
    if (coins[i] <= change) {
      answer += Math.floor(change / coins[i]);
      change %= coins[i];
    }
  }
  return answer;
}

console.log(solution());