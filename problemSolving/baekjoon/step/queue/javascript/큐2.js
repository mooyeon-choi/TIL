const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n")
  .map((line) => line.split(" "));

const N = Number(input[0][0]);
const request = input.slice(1);

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

  front() {
    if (this.head >= this.items.length) {
      return -1;
    }

    return this.items[this.head];
  }

  back() {
    if (this.head >= this.items.length) {
      return -1;
    }
    return this.items[this.items.length - 1];
  }

  size() {
    return this.items.length - this.head;
  }
}

function solution(n, req) {
  const queue = new Queue();
  const answer = [];

  for (let i = 0; i < n; i++) {
    const [command, value] = req[i];

    switch (command) {
      case "push":
        queue.enqueue(Number(value));
        break;
      case "pop":
        const poppedValue = queue.dequeue();
        answer.push(poppedValue);
        break;
      case "size":
        answer.push(queue.size());
        break;
      case "empty":
        answer.push(queue.isEmpty());
        break;
      case "front":
        answer.push(queue.front());
        break;
      case "back":
        answer.push(queue.back());
        break;
      default:
        break;
    }
  }

  return answer;
}

console.log(solution(N, request).join("\n"));