const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n")
  .map(arr => arr.split(" ").map(Number));

const [N, M] = input[0];
const nodes = input.slice(1);

const graph = new Map();

for (const [a, b] of nodes) {
  if (!graph.has(a)) graph.set(a, []);
  if (!graph.has(b)) graph.set(b, []);

  graph.get(a).push(b);
  graph.get(b).push(a);
}

let visited = Array(N + 1).fill(false);

function dfs(v) {
  visited[v] = true;
  for (const node of graph.get(v) || []) {
    if (!visited[node]) dfs(node);
  }
}

let result = 0;

for (let i = 1; i <= N; i++) {
  if (!visited[i]) {
    dfs(i);
    result++;
  }
}

console.log(result);