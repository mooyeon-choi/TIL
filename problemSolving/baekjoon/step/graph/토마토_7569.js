const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n");

const [M, N, H] = input[0].split(" ").map(Number);
const nodes = input.slice(1).map(arr => arr.split(" ").map(Number));
const tomatoes = [];

for (let i = 0; i < H; i++) {
  tomatoes.push([]);
  for (let j = 0; j < N; j++) {
    tomatoes[i].push([]);
    for (let k = 0; k < M; k++) {
      if (nodes[j + i * N][k] === 1) {
        tomatoes[i][j].push(1);
      } else if (nodes[j + i * N][k] === 0) {
        tomatoes[i][j].push(0);
      } else {
        tomatoes[i][j].push(-1);
      }
    }
  }
}


const dirs = [
  [0, 0, 1],
  [0, 0, -1],
  [0, 1, 0],
  [0, -1, 0],
  [1, 0, 0],
  [-1, 0, 0],
];

function bfs(tomatoes, H, N, M) {
  const queue = [];

  for (let i = 0; i < H; i++) {
    for (let j = 0; j < N; j++) {
      for (let k = 0; k < M; k++) {
        if (tomatoes[i][j][k] === 1) {
          queue.push([i, j, k]);
        }
      }
    }
  }

  let head = 0;
  while (head < queue.length) {
    const [z, y, x] = queue[head++];
    for (const [dz, dy, dx] of dirs) {
      const nz = z + dz;
      const ny = y + dy;
      const nx = x + dx;
      if (nz >= 0 && nz < H && ny >= 0 && ny < N && nx >= 0 && nx < M && tomatoes[nz][ny][nx] === 0) {
        tomatoes[nz][ny][nx] = tomatoes[z][y][x] + 1;
        queue.push([nz, ny, nx]);
      }
    }
  }

  for (let i = 0; i < H; i++) {
    for (let j = 0; j < N; j++) {
      for (let k = 0; k < M; k++) {
        if (tomatoes[i][j][k] === 0) {
          return -1;
        }
      }
    }
  }

  let maxValue = -Infinity;
  for (let i = 0; i < H; i++) {
    for (let j = 0; j < N; j++) {
      for (let k = 0; k < M; k++) {
        maxValue = Math.max(maxValue, tomatoes[i][j][k]);
      }
    }
  }
  
  return maxValue - 1;
} 

console.log(bfs(tomatoes, H, N, M));