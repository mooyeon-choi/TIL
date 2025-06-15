const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n")
  .map(Number);

const N = input[0];
const numbers = input.slice(1);

function bubbleSort(n, nums) {
  const answer = [...nums];
  
  for (let i = 0; i < n - 1; i++) {
    for (let j = 0; j < n - i - 1; j++) {
      if (answer[j] > answer[j + 1]) {
        [answer[j], answer[j + 1]] = [answer[j + 1], answer[j]];
      }
    }
  }

  return answer;
}

console.log(bubbleSort(N, numbers).join("\n"));