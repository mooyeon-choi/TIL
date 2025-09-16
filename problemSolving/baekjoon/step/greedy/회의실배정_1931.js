const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n");

const N = Number(input[0]);
const meetings = input.slice(1).map(line => line.split(" ").map(Number));

function solution() {
  meetings.sort((a, b) => {
    if (a[1] === b[1]) return a[0] - b[0];
    return a[1] - b[1];
  });
  let answer = 0;
  let memo = -1;

  for (const [start, end] of meetings) {
    if (start >= memo) {
      answer++;
      memo = end;
    }
  }

  return answer;
}

console.log(solution());