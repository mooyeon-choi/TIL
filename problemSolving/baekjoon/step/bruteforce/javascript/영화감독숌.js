const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim();

const num = Number(input);

function find(n) {
  let count = 0;
  let num = 665;
  while (true) {
    num++;
    
    if (num.toString().includes("666")) {
      count++;
    }
    if (count === n) {
      return num;
    }
  }
}

console.log(find(num));