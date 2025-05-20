const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n")

const [N, M] = input[0].split(" ").map(Number)
const board = input.slice(1)

function checkBoard(board, x, y, color) {
  let count = 0

  for (let i = x; i < x + 8; i++) {
    for (let j = y; j < y + 8; j++) {
      if ((i + j) % 2 === 0 && board[i][j] !== color) {
        count++
      } else if ((i + j) % 2 === 1 && board[i][j] === color) {
        count++
      }
    }
  }

  return count
}

function getMinCount(board, N, M) {
  let minCount = 64;

  for (let i = 0; i <= N - 8; i++) {
    for (let j = 0; j <= M - 8; j++) {
      const count1 = checkBoard(board, i, j, "W")
      const count2 = checkBoard(board, i, j, "B")

      if (count1 < minCount) {
        minCount = count1
      }
      if (count2 < minCount) {
        minCount = count2
      }
    }
  }

  return minCount
}

console.log(getMinCount(board, N, M))
