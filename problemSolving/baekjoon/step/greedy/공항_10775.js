const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n")
  .map(Number);

const G = input[0];
const P = input[1];
const gates = input.slice(2);

function solution() {
  let answer = 0;
  const next = Array.from({ length: G + 1 }, (_, i) => i);

  function getNext(x) {
    while (x > 0 && next[x] !== x) {
      next[x] = next[next[x]];
      x = next[x];
    }
    return x;
  }

  for (let i = 0; i < P; i++) {
    const g = gates[i];
    let pos = getNext(g);
    if (pos === 0) break;
    next[pos] = pos - 1;
    answer++;
  }

  return answer;
}

console.log(solution());