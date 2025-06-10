const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split(" ")
  .map(Number);

const N = input[0];
const K = input[1];

class Queue {
  constructor() {
    this.items = [];
    this.head = 0;
  }

  enqueue(item) {
    this.items.push(item);
  }

  dequeue() {
    if (this.head >= this.items.length) {
      return -1;
    }
    const item = this.items[this.head];
    this.head++;
    return item;
  }

  isEmpty() {
    return this.items.length <= this.head ? 1 : 0;
  }
}

function solution(n, k) {
  const queue = new Queue();
  const answer = [];
  for (let i = 1; i <= n; i++) {
    queue.enqueue(i);
  }

  while (!queue.isEmpty()) {
    for (let i = 0; i < k - 1; i++) {
      queue.enqueue(queue.dequeue());
    }
    answer.push(queue.dequeue());
  }

  return answer.join(", ");
}

console.log(`<${solution(N, K)}>`);