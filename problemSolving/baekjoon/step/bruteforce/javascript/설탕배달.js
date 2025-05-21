const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim();

const num = Number(input);

function find(n) {
  for (let i = 0; i <= n / 3; i++) {
    for (let j = 0; j <= n / 5; j++) {
      if (i * 3 + j * 5 === n) {
        return i + j;
      }
    }
  }
  return -1;
}

console.log(find(num));