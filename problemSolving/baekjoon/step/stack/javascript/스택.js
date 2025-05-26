const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n");

const N = Number(input[0]);
const commands = input.slice(1).map((el) => el.split(" "));

function stackOperations(commands) {
  const stack = [];
  const result = [];

  commands.forEach((command) => {
    switch (command[0]) {
      case "push":
        stack.push(Number(command[1]));
        break;
      case "pop":
        result.push(stack.length ? stack.pop() : -1);
        break;
      case "size":
        result.push(stack.length);
        break;
      case "empty":
        result.push(stack.length === 0 ? 1 : 0);
        break;
      case "top":
        result.push(stack.length ? stack[stack.length - 1] : -1);
        break;
    }
  });

  return result.join("\n");
}

console.log(stackOperations(commands));