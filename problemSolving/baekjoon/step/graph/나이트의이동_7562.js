const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n");

const dirs = [
  [-2, -1],
  [-1, -2],
  [1, -2],
  [2, -1],
  [2, 1],
  [1, 2],
  [-1, 2],
  [-2, 1],
];

const N = Number(input[0]);
const cases = input.slice(1);

function bfs(size, start, end) {
  const queue = [start];
  const visited = Array.from({ length: size }, () => Array(size).fill(false));
  visited[start[0]][start[1]] = true;
  let moves = 0;

  while (queue.length) {
    const L = queue.length;
    for (let i = 0; i < L; i++) {
      const [x, y] = queue.shift();
      if (x === end[0] && y === end[1]) return moves;

      for (const [dx, dy] of dirs) {
        const nx = x + dx;
        const ny = y + dy;
        if (nx >= 0 && ny >= 0 && nx < size && ny < size && !visited[nx][ny]) {
          visited[nx][ny] = true;
          queue.push([nx, ny]);
        }
      }
    }
    moves++;
  }
  return 0;
}

for (let i = 0; i < N; i++) {
  const I = Number(cases[i * 3]);
  const start = cases[i * 3 + 1].split(" ").map(Number);
  const end = cases[i * 3 + 2].split(" ").map(Number);
  const result = bfs(I, start, end);
  console.log(result);
}