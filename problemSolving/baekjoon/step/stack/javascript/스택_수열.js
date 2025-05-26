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
  const answer = [];

  let num = 1;
  for (let i = 0; i < n; i++) {
    if (stack.length === 0 || stack[stack.length - 1] < nums[i]) {
      while (num <= nums[i]) {
        stack.push(num);
        answer.push("+");
        num++;
      }
    } else if (stack[stack.length - 1] > nums[i]) {
      return ["NO"];
    }

    if (stack[stack.length - 1] === nums[i]) {
      stack.pop();
      answer.push("-");
    }
  }
  
  return answer;
}

console.log(find(N, numbers).join("\n"));
