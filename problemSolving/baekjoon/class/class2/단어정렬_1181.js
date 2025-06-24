const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n");

const N = Number(input[0]);
const words = input.slice(1).map((word) => word.trim());

function solution(words) {
  const uniqueWords = new Set(words);
  return [...uniqueWords].sort((a, b) => {
    if (a.length === b.length) {
      return a.localeCompare(b);
    }
    return a.length - b.length;
  });
}

console.log(solution(words).join("\n"));
