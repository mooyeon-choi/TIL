const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n");

const [N, M] = input[0].split(" ").map(Number);
const nodes = input.slice(1).map(arr => arr.split("").map(Number));

const memos = Array.from({ length: N }, () => Array(M).fill(10000));

function bfs(x, y) {
  const queue = [[x, y]];
  let head = 0;
  memos[x][y] = 1;

  while (head < queue.length) {
    const [x, y] = queue[head++];

    if (x === N - 1 && y === M - 1) return memos[x][y];

    if (x + 1 < N && nodes[x + 1][y] === 1 && memos[x + 1][y] > memos[x][y] + 1) {
      memos[x + 1][y] = memos[x][y] + 1;
      queue.push([x + 1, y]);
    }

    if (x - 1 >= 0 && nodes[x - 1][y] === 1 && memos[x - 1][y] > memos[x][y] + 1) {
      memos[x - 1][y] = memos[x][y] + 1;
      queue.push([x - 1, y]);
    }

    if (y + 1 < M && nodes[x][y + 1] === 1 && memos[x][y + 1] > memos[x][y] + 1) {
      memos[x][y + 1] = memos[x][y] + 1;
      queue.push([x, y + 1]);
    }

    if (y - 1 >= 0 && nodes[x][y - 1] === 1 && memos[x][y - 1] > memos[x][y] + 1) {
      memos[x][y - 1] = memos[x][y] + 1;
      queue.push([x, y - 1]);
    }
  }
}

bfs(0, 0)
console.log(memos[N - 1][M - 1]);