const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim();

const N = Number(input);

function dfs(memo, cnt) {
  if (cnt === N) return memo.reduce((prev, curr) => (prev + curr), 0) % 1000000000;
  return dfs([memo[1], (memo[0] + memo[2]) % 1000000000, memo[1] + memo[3] % 1000000000, memo[2] + memo[4] % 1000000000, memo[3] + memo[5] % 1000000000, memo[4] + memo[6] % 1000000000, memo[5] + memo[7] % 1000000000, memo[6] + memo[8] % 1000000000, memo[7] + memo[9] % 1000000000, memo[8]], cnt + 1);
}

console.log(dfs([0, 1, 1, 1, 1, 1, 1, 1, 1, 1], 1));