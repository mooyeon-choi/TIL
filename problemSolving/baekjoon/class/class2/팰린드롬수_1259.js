const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n");

function isPalindrome(str) {
  for (let i = 0; i < str.length / 2; i++) {
    if (str[i] !== str[str.length - 1 - i]) {
      return "no";
    }
  }
  return "yes";
}

function solution(input) {
  const results = [];
  for (const line of input) {
    if (line === "0") break;
    results.push(isPalindrome(line));
  }
  return results.join("\n");
}

console.log(solution(input));