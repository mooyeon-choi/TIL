const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n")
  .map((el) => el.split(" ").map(Number));

const N = input[0];
const numbers = input.slice(1);

function find(n, nums) {
  const stack = [];
  const answer = [];
  
  for (let i = 0; i < n; i++) {
    switch (nums[i][0]) {
      case 1: // push
        stack.push(nums[i][1]);
        break;
      case 2: // pop
        if (stack.length === 0) {
          answer.push(-1);
        } else {
          answer.push(stack.pop());
        }
        break;
      case 3: // size
        answer.push(stack.length);
        break;
      case 4: // empty
        answer.push(stack.length === 0 ? 1 : 0);
        break;
      case 5: // top
        if (stack.length === 0) {
          answer.push(-1);
        } else {
          answer.push(stack[stack.length - 1]);
        }
        break;
    }
  }

  return answer;
}

console.log(find(N, numbers).join("\n"));