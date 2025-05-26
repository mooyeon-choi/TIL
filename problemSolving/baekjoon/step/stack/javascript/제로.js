const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n")
  .map(Number);

const N = input[0];
const numbers = input.slice(1);

function find(n, nums) {
  const stack = [];

  nums.forEach((num, i) => {
    if (num === 0) {
      if (stack.length > 0) {
        stack.pop();
      }
    }
    else {
      stack.push(num);
    }
  }
  );
  
  return stack.reduce((acc, cur) => acc + cur, 0);
}

console.log(find(N, numbers));
