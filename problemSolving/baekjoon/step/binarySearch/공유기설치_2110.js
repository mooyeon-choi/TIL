const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n");

const [N, C] = input[0].split(" ").map(Number);
const positions = input.slice(1).map(Number).sort((a, b) => a - b);

const solution = () => {
  let left = 1;
  let right = positions[N - 1] - positions[0];
  let mid = Math.floor((left + right) / 2);

  while (left <= right) {
    mid = Math.floor((left + right) / 2);
    let cnt = 1;
    let lastPosition = positions[0];

    for (let i = 1; i < N; i++) {
      if (positions[i] - lastPosition >= mid) {
        cnt++;
        lastPosition = positions[i];
      }
    }

    if (cnt >= C) {
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }

  return left - 1;
}

console.log(solution());