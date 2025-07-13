const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n")
  .map(arr => arr.split(" ").map(Number));

const N = input[0][0];
const nodes = input.slice(1);

let visited;

function bfs(x, y, height) {
  const queue = [[x, y]];
  let head = 0;
  visited[x][y] = 1;

  while (head < queue.length) {
    const [x, y] = queue[head++];

    if (x + 1 < N && nodes[x + 1][y] > height && visited[x + 1][y] === 0) {
      visited[x + 1][y] = 1;
      queue.push([x + 1, y]);
    }

    if (x - 1 >= 0 && nodes[x - 1][y] > height && visited[x - 1][y] === 0) {
      visited[x - 1][y] = 1;
      queue.push([x - 1, y]);
    }

    if (y + 1 < N && nodes[x][y + 1] > height && visited[x][y + 1] === 0) {
      visited[x][y + 1] = 1;
      queue.push([x, y + 1]);
    }

    if (y - 1 >= 0 && nodes[x][y - 1] > height && visited[x][y - 1] === 0) {
      visited[x][y - 1] = 1;
      queue.push([x, y - 1]);
    }
  }
}

function solution() {
  let result = 0;
  for (let height = 0; height < 100; height++) {
    visited = Array.from({ length: N }, () => Array(N).fill(0));
    let count = 0;
    for (let i = 0; i < N; i++) {
      for (let j = 0; j < N; j++) {
        if (nodes[i][j] > height && visited[i][j] === 0) {
          bfs(i, j, height);
          count++;
        }
      }
    }
    result = Math.max(result, count);
  }
  return result;
}

console.log(solution());