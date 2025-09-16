const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n")
  .map(arr => arr.split(" ").map(Number));

const [N, M] = input[0];
const items = input;
const dp = Array.from({ length: N + 1 }, () => Array(M + 1).fill(0));

function solution() {
  for (let i = 1; i <= N; i++) {
    for (let j = 1; j <= M; j++) {
      if (j < items[i][0]) dp[i][j] = dp[i - 1][j];
      else dp[i][j] = Math.max(dp[i - 1][j], dp[i - 1][j - items[i][0]] + items[i][1]);
    }
  }
  return dp[N][M];
}

console.log(solution());