const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n");

const T = Number(input[0]);
const nodes = input.slice(1).map(arr => arr.split(" ").map(Number));

function D(num) {
  return (num * 2) % 10000;
}

function S(num) {
  return num === 0 ? 9999 : num - 1;
}

function L(num) {
  return (num % 1000) * 10 + Math.floor(num / 1000);
}

function R(num) {
  return (num % 10) * 1000 + Math.floor(num / 10);
}

for (const [A, B] of nodes) {
  const visited = Array(10000).fill(false);
  const queue = [[A, ""]];
  let head = 0;

  while (head < queue.length) {
    const [num, path] = queue[head];

    if (num === B) {
      console.log(path);
      break;
    }

    if (!visited[D(num)]) {
      visited[D(num)] = true;
      queue.push([D(num), path + "D"]);
    }

    if (!visited[S(num)]) {
      visited[S(num)] = true;
      queue.push([S(num), path + "S"]);
    }

    if (!visited[L(num)]) {
      visited[L(num)] = true;
      queue.push([L(num), path + "L"]);
    }

    if (!visited[R(num)]) {
      visited[R(num)] = true;
      queue.push([R(num), path + "R"]);
    }

    head++;
  }
}
