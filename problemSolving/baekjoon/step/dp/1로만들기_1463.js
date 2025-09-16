const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim();

const N = Number(input);

const memo = [0, 0];

for (let i = 2; i <= N; i++) {
  let now = memo[i - 1] + 1
  if (i % 3 === 0) {
    now = Math.min(memo[i], memo[i / 3] + 1);
  }
  if (i % 2 === 0) {
    now = Math.min(memo[i], memo[i / 2] + 1);
  }
  memo.push(now);
}

console.log(memo[N]);