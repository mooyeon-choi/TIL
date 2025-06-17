const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n")
  .map(line => line.split(" ").map(Number));

const N = input[0][0];
const nums = input[1];

function solution(n, num) {
  const answer = [];
  const numSet = new Set(num);
  const sortedNums = [...numSet]
    .sort((a, b) => a - b);

  for (let i = 0; i < n; i++) {
    const rank = sortedNums.indexOf(num[i]);
    answer.push(rank);
  }

  return answer.join(" ");
}

console.log(solution(N, nums));