const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n")
  .map((line) => line.split(" ").map(Number));

const N = input[0][0];
const request = input.slice(1);

class Node {
  constructor(value) {
    this.value = value;
    this.prev = null;
    this.next = null;
  }
}

class Deque {
  constructor() {
    this.head = null;
    this.tail = null;
    this.size = 0;
  }

  push(value) {
    const newNode = new Node(value);
    if (!this.head) {
      this.head = newNode;
      this.tail = newNode;
      newNode.next = newNode;
      newNode.prev = newNode;
    } else {
      newNode.prev = this.tail;
      newNode.next = this.head;
      this.tail.next = newNode;
      this.head.prev = newNode;
      this.tail = newNode;
    }
    this.size++;
  }

  pushFront(value) {
    const newNode = new Node(value);
    if (!this.head) {
      this.head = newNode;
      this.tail = newNode;
      newNode.next = newNode;
      newNode.prev = newNode;
    } else {
      newNode.prev = this.tail;
      newNode.next = this.head;
      this.tail.next = newNode;
      this.head.prev = newNode;
      this.head = newNode;
    }
    this.size++;
  }

  pop() {
    if (this.size === 0) return -1;
    const item = this.tail;
    if (this.size === 1) {
      this.head = null;
      this.tail = null;
    } else {
      this.tail = this.tail.prev;
      this.tail.next = this.head;
      this.head.prev = this.tail;
    }
    this.size--;
    return item.value;
  }

  dequeue() {
    if (this.size === 0) return -1;
    const item = this.head;
    if (this.size === 1) {
      this.head = null;
      this.tail = null;
    } else {
      this.head = this.head.next;
      this.head.prev = this.tail;
      this.tail.next = this.head;
    }
    this.size--;
    return item.value;
  }

  front() {
    return this.size === 0 ? -1 : this.head.value;
  }

  back() {
    return this.size === 0 ? -1 : this.tail.value;
  }

  isEmpty() {
    return this.size === 0 ? 1 : 0;
  }
}

function solution(n, req) {
  const deque = new Deque();
  const answer = [];
  
  req.forEach(element => {
    switch (element[0]) {
      case 1:
        deque.pushFront(element[1]);
        break;
      case 2:
        deque.push(element[1]);
        break;
      case 3:
        answer.push(deque.dequeue());
        break;
      case 4:
        answer.push(deque.pop());
        break;
      case 5:
        answer.push(deque.size);
        break;
      case 6:
        answer.push(deque.isEmpty());
        break;
      case 7:
        answer.push(deque.front());
        break;
      case 8:
        answer.push(deque.back());
        break;
      default:
        break;
    }
  });
  return answer.join('\n');
}

console.log(solution(N, request));