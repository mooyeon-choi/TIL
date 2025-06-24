const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n");

const A = input[0];
const B = input[1];

function solution(a, b) {
  const aMap = new Map();
  const bMap = new Map();
  const resultMap = new Map();
  
  for (const char of a) {
    aMap.set(char, (aMap.get(char) || 0) + 1);
  }
  for (const char of b) {
    bMap.set(char, (bMap.get(char) || 0) + 1);
  }

  for (const [char, count] of aMap) {
    if (bMap.has(char)) {
      const maxCount = Math.max(count, bMap.get(char));
      resultMap.set(char, maxCount);
    } else {
      resultMap.set(char, count);
    }
  }

  for (const [char, count] of bMap) {
    if (!resultMap.has(char)) {
      resultMap.set(char, count);
    }
  }

  const result = [];

  for (const [char, count] of resultMap) {
    result.push(char.repeat(count));
  }

  return result.join('');
}

console.log(solution(A, B));