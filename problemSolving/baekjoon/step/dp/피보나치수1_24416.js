const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim();

const N = input;

let cnt = 0;

function fibonacci(n) {
  const dp = Array.from({ length: n + 1 }, () => 0);
  dp[1] = dp[2] = 1;
  for (let i = 3; i <= n; i++) {
    dp[i] = dp[i - 1] + dp[i - 2];
    cnt++;
  }
  return dp[n];
}

const result = fibonacci(N);

console.log(result, cnt);