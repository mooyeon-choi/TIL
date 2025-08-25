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
  const memo = new Set(Array(G + 1).fill(0).map((_, i) => i));

  for (let i = 0; i < P; i++) {
    let num = gates[i];
    while (!memo.has(num) && num > 0) {
      num--;
    }
    if (num === 0) break;
    memo.delete(num);
    answer++;
  }

  return answer;
}

console.log(solution());