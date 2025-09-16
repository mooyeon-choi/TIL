const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n");

const N = Number(input[0]);
const arr = input[1].split(" ");

function solution() {
  arr.sort((a, b) => {
    if (a.length < b.length) {
      const repeatB = b.repeat(2);
      const repeatA = a.repeat(Math.ceil(b.length * 2 / a.length));
      return  Number(repeatB) - Number(repeatA.substring(0, repeatB.length));
    } else {
      const repeatA = a.repeat(2);
      const repeatB = b.repeat(Math.ceil(a.length * 2 / b.length));
      return Number(repeatB.substring(0, repeatA.length)) - Number(repeatA);
    }
  });
  let result = arr.join("");
  let idx = 0;

  while (result[idx] === "0" && idx < result.length - 1) {
    idx++;
  }

  return result.substring(idx);
}

console.log(solution());