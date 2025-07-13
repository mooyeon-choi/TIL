const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n");

const [N, M] = input[0].split(" ").map(Number);
const nodes = input.slice(1).map(arr => arr.split("").map(Number));

const visited = Array.from({ length: N }, () => Array.from({ length: M }, () => [1000000, 1000000]));

function bfs(x, y) {
  const queue = [[x, y]];
  visited[x][y] = [1, 1];
  let head = 0;

  while (head < queue.length) {
    const [x, y] = queue[head];

    if (x === N - 1 && y === M - 1) return Math.min(visited[x][y][0], visited[x][y][1]);

    // 벽을 부수지 않고 이동
    if (x + 1 < N && nodes[x + 1][y] === 0 && visited[x + 1][y][0] > visited[x][y][0] + 1) {
      visited[x + 1][y][0] = visited[x][y][0] + 1;
      queue.push([x + 1, y]);
    }

    if (x - 1 >= 0 && nodes[x - 1][y] === 0 && visited[x - 1][y][0] > visited[x][y][0] + 1) {
      visited[x - 1][y][0] = visited[x][y][0] + 1;
      queue.push([x - 1, y]);
    }

    if (y + 1 < M && nodes[x][y + 1] === 0 && visited[x][y + 1][0] > visited[x][y][0] + 1) {
      visited[x][y + 1][0] = visited[x][y][0] + 1;
      queue.push([x, y + 1]);
    }

    if (y - 1 >= 0 && nodes[x][y - 1] === 0 && visited[x][y - 1][0] > visited[x][y][0] + 1) {
      visited[x][y - 1][0] = visited[x][y][0] + 1;
      queue.push([x, y - 1]);
    }

    // 벽을 부수고 이동
    if (x + 1 < N && nodes[x + 1][y] === 1 && visited[x + 1][y][1] > visited[x][y][0] + 1) {
      visited[x + 1][y][1] = visited[x][y][0] + 1;
      queue.push([x + 1, y]);
    }

    if (x - 1 >= 0 && nodes[x - 1][y] === 1 && visited[x - 1][y][1] > visited[x][y][0] + 1) {
      visited[x - 1][y][1] = visited[x][y][0] + 1;
      queue.push([x - 1, y]);
    }

    if (y + 1 < M && nodes[x][y + 1] === 1 && visited[x][y + 1][1] > visited[x][y][0] + 1) {
      visited[x][y + 1][1] = visited[x][y][0] + 1;
      queue.push([x, y + 1]);
    }

    if (y - 1 >= 0 && nodes[x][y - 1] === 1 && visited[x][y - 1][1] > visited[x][y][0] + 1) {
      visited[x][y - 1][1] = visited[x][y][0] + 1;
      queue.push([x, y - 1]);
    }

    // 이미 벽을 부수고 방문한 경우
    if (x + 1 < N && nodes[x + 1][y] === 0 && visited[x + 1][y][1] > visited[x][y][1] + 1) {
      visited[x + 1][y][1] = visited[x][y][1] + 1;
      queue.push([x + 1, y]);
    }

    if (x - 1 >= 0 && nodes[x - 1][y] === 0 && visited[x - 1][y][1] > visited[x][y][1] + 1) {
      visited[x - 1][y][1] = visited[x][y][1] + 1;
      queue.push([x - 1, y]);
    }

    if (y + 1 < M && nodes[x][y + 1] === 0 && visited[x][y + 1][1] > visited[x][y][1] + 1) {
      visited[x][y + 1][1] = visited[x][y][1] + 1;
      queue.push([x, y + 1]);
    }

    if (y - 1 >= 0 && nodes[x][y - 1] === 0 && visited[x][y - 1][1] > visited[x][y][1] + 1) {
      visited[x][y - 1][1] = visited[x][y][1] + 1;
      queue.push([x, y - 1]);
    }

    head++;
  }

  return -1;
}

console.log(bfs(0, 0));