const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n")
  .map(arr => arr.split(" ").map(Number));

const [N, M, V] = input[0];
const nodes = input.slice(1);

const graph = new Map();

for (const [a, b] of nodes) {
  if (!graph.has(a)) graph.set(a, []);
  if (!graph.has(b)) graph.set(b, []);

  graph.get(a).push(b);
  graph.get(b).push(a);
}

let visited = Array(N + 1).fill(false);
let result = [];

function dfs(v) {
  visited[v] = true;
  result.push(v);
  for (const node of (graph.get(v) || []).sort((a, b) => a - b)) {
    if (!visited[node]) dfs(node);
  }
}

dfs(V);
console.log(result.join(" "));

visited = Array(N + 1).fill(false);
result = [];

function bfs(v) {
  const queue = [v];
  visited[v] = true;

  while (queue.length > 0) {
    const current = queue.shift();
    result.push(current);
    for (const node of (graph.get(current) || []).sort((a, b) => a - b)) {
      if (visited[node]) continue;
      visited[node] = true;
      queue.push(node);
    }
  }
}

bfs(V);
console.log(result.join(" "));