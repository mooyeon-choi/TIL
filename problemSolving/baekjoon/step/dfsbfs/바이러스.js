const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n")
  .map(arr => arr.split(" ").map(Number));

const N = input[0][0];
const M = input[1][0];
const nodes = input.slice(2);

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

dfs(1);
console.log(visited.filter(v => v).length - 1);