const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim();

const N = Number(input);

let answer = 0;

function dfx(arr) {
  if (arr.length === N) {
    answer++;
    return;
  }
  for (let i = 0; i < N; i++) {
    if (arr.includes(i)) continue;
    let flag = true;
    for (let j = 0; j < arr.length; j++) {
      if (arr[j] - (arr.length - j) === i || arr[j] + (arr.length - j) === i) {
        flag = false;
        break;
      }
    }
    if (flag) dfx([...arr, i]);
  }
}

dfx([]);

console.log(answer);