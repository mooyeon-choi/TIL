const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split(" ")
  .map((el) => Number(el));

const [A, B, C, D, E, F] = input;

function find(a, b, c, d, e, f) {
  for (let i = -999; i <= 999; i++) {
    for (let j = -999; j <= 999; j++) {
      if (a * i + b * j === c && d * i + e * j === f) {
        return [i, j];
      }
    }
  }
  return null;
}

console.log(find(A, B, C, D, E, F).join(" "));