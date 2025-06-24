const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n")
  .map(Number);

const N = input[0];
const NUMS = input.slice(1);

class TreeNode {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }

  setLeft(value) {
    this.left = value;
  }

  setRight(value) {
    this.right = value;
  }
}

function solution(n, nums) {
  let root = null;
  const result = [];

  for (let i = 0; i < n; i++) {
    if (nums[i] === 0) {
      if (root === null) {
        result.push(0);
      } else {
        result.push(root.value);
        if (root.left === null) {
          root = null;
        } else {
          root = root.left;
        }
      }
    } else {
      const node = new TreeNode(nums[i]);
      const nodes = [];
      if (root === null) {
        root = node;
      } else {
        nodes.push(root);
        while (nodes.length > 0) {
          const current = nodes.shift();
          if (node.value > current.value) {
            if (current.right === null) {
              current.setRight(node);
              break;
            } else {
              nodes.push(current.right);
            }
          } else {
            if (current.left === null) {
              current.setLeft(node);
              break;
            } else {
              nodes.push(current.left);
            }
          }
        }
      }
    }
  }

  return result.join("\n");
}

console.log(solution(N, NUMS));