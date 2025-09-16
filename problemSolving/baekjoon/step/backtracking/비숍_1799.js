const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n");

const N = Number(input[0]);
const board = input.slice(1).map((line) => line.split(" ").map(Number));

let answer = 0;

function dfs(arr) {
  if (arr.length > answer) answer = arr.length;
  let startI = 0;
  let startJ = 0;

  if (arr.length > 0 && arr[arr.length - 1][1] < N - 1) {
    startJ = arr[arr.length - 1][1] + 1;
  } else {
    startI = arr.length > 0 ? arr[arr.length - 1][0] + 1 : 0;
  }

  for (let i = startI; i < N; i++) {
    for (let j = 0; j < N; j++) {
      if (i === startI) {
        if (j < startJ) continue;
      }
      let flag = false;
      if (board[i][j] === 1) {
        for (let k = 0; k < arr.length; k++) {
          if (Math.abs(arr[k][0] - i) === Math.abs(arr[k][1] - j)) {
            flag = true;
            break;
          }
        }
        if (flag) continue;
        board[i][j] = 0;
        dfs([...arr, [i, j]]);
      }
    }
  }
}

dfs([]);

console.log(answer);