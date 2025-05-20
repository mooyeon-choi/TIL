const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()

const num = Number(input);

function find(n) {
    for (let i = 0; i < num; i++) {
        if (i + i.toString().split('').reduce((prev, curr) => prev + Number(curr), 0) === num) {
            return i;
        }
    }
    return 0;
}

console.log(find(num));