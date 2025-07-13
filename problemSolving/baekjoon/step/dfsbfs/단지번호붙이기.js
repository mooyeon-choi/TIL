const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n")
  ;

const N = Number(input[0]);
const nodes = input.slice(1).map(arr => arr.split("").map(Number));

function dfs(x, y) {
  if (x < 0 || x >= N || y < 0 || y >= N) return 0;
  if (nodes[x][y] === 0) return 0;

  let result = 1;
  nodes[x][y] = 0;
  result += dfs(x + 1, y);
  result += dfs(x - 1, y);
  result += dfs(x, y + 1);
  result += dfs(x, y - 1);
  return result;
}

const answer = [];

for (let i = 0; i < N; i++) {
  for (let j = 0; j < N; j++) {
    if (nodes[i][j]) {
      answer.push(dfs(i, j));
    }
  }
}

console.log(answer.length)
console.log(answer.sort((a, b) => a - b).join("\n"));