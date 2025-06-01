// 큐 구현

class Queue {
  constructor() {
    this.items = [];
    this.head = 0;
  }

  enqueue(item) {
    this.items.push(item);
  }

  dequeue() {
    if (this.isEmpty()) return undefined;
    const value = this.items[this.head];
    this.head += 1;

    if (this.head > 1000) {
        this.items = this.items.slice(this.head);
        this.head = 0;
      }
    return value;
  }

  peek() {
    return this.items[this.head];
  }

  isEmpty() {
    return this.items.length === this.head;
  }
}

const queue = new Queue();

queue.enqueue(1);
queue.enqueue(2);
queue.enqueue(3);

console.log(queue.dequeue());

