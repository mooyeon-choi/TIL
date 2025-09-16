const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split(" ")
  .map(Number);

const N = input[0];
const M = input[1];

function dfs(arr) {
  if (arr.length < M) {
    for (let i = 1; i <= N; i++) {
      if (!arr.includes(i)) dfs([...arr, i]);
    }
  } else {
    console.log(arr.join(' '))
  }
}

dfs([]);