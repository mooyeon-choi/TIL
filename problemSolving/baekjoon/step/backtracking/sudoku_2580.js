const board = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n")
  .map((line) => line.split(" ").map(Number));

function isValid(board, row, col, num) {
  for (let i = 0; i < 9; i++) {
    if (board[row][i] === num || board[i][col] === num)
      return false;
  }
  for (let i = Math.floor(row / 3) * 3; i < Math.floor(row / 3) * 3 + 3; i++) {
    for (let j = Math.floor(col / 3) * 3; j < Math.floor(col / 3) * 3 + 3; j++) {
      if (board[i][j] === num) return false;
    }
  }
  return true;
}

function dfs() {
  for (let i = 0; i < 9; i++) {
    for (let j = 0; j < 9; j++) {
      if (board[i][j] === 0) {
        for (let num = 1; num <= 9; num++) {
          if (isValid(board, i, j, num)) {
            board[i][j] = num;
            if (dfs(board)) return true;
            board[i][j] = 0;
          }
        }
        return false;
      }
    }
  }
  return true;
}

dfs();

console.log(board.map((row) => row.join(" ")).join("\n"));