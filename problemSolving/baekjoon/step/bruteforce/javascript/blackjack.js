const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n")
  .map((el) => el.split(" ").map(Number));

const [N, M] = input[0];
const numbers = input[1];

function find(n, m, nums) {
  let answer = 0;
  let sum;

  for (let i = 0; i < N; i++) {
    for (let j = i + 1; j < N; j++) {
      for (let k = j + 1; k < N; k++) {
        sum = numbers[i] + numbers[j] + numbers[k];

        if (sum <= M && sum > answer) {
          answer = sum;
        }
      }
    }
  }
  return answer;
}

console.log(find(N, M, numbers));

