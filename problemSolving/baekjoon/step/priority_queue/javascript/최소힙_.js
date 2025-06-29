const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n")
  .map(Number);

const N = input[0];
const NUMS = input.slice(1);

class PriorityQueue {
  #compare = (a, b) => a - b;
  #heap = new Array(64);
  #setPosition;
  #size = 0;

  constructor(comparator, setPosition) {
    if (comparator !== undefined)
      this.#compare = comparator;
    if (setPosition !== undefined)
      this.#setPosition = setPosition;
  }

  insert(value) {
    const heap = this.#heap;
    const pos = ++this.#size;
    heap[pos] = value;

    if (heap.length === pos)
      heap.length *= 2;

    this.percolateUp(pos);
  }

  peek() {
    return this.#heap[1];
  }

  peekBottom() {
    return this.#heap[this.#size];
  }

  percolateDown(pos) {
    const compare = this.#compare;
    const setPosition = this.#setPosition;
    const heap = this.#heap;
    const size = this.#size;
    const item = heap[pos];

    while (pos * 2 <= size) {
      let childIndex = pos * 2 + 1;
      if (childIndex > size || compare(heap[pos * 2], heap[childIndex]) < 0)
        childIndex = pos * 2;
      const child = heap[childIndex];
      if (compare(item, child) <= 0)
        break;
      if (setPosition !== undefined)
        setPosition(child, pos);
      heap[pos] = child;
      pos = childIndex;
    }
    heap[pos] = item;
    if (setPosition !== undefined)
      setPosition(item, pos);
  }

  percolateUp(pos) {
    const heap = this.#heap;
    const compare = this.#compare;
    const setPosition = this.#setPosition;
    const item = heap[pos];

    while (pos > 1) {
      const parent = heap[pos / 2 | 0];
      if (compare(parent, item) <= 0)
        break;
      heap[pos] = parent;
      if (setPosition !== undefined)
        setPosition(parent, pos);
      pos = pos / 2 | 0;
    }
    heap[pos] = item;
    if (setPosition !== undefined)
      setPosition(item, pos);
  }

  removeAt(pos) {
    const heap = this.#heap;
    const size = --this.#size;
    heap[pos] = heap[size + 1];
    heap[size + 1] = undefined;

    if (size > 0 && pos <= size) {
      if (pos > 1 && this.#compare(heap[pos / 2 | 0], heap[pos]) > 0)
        this.percolateUp(pos);
      else
        this.percolateDown(pos);
    }
  }

  shift() {
    const heap = this.#heap;
    const value = heap[1];
    if (value === undefined)
      return;

    this.removeAt(1);

    return value;
  }
};

function solution(n, nums) {
  const pq = new PriorityQueue();
  const answer = [];

  for (let i = 0; i < n; i++) {
    if (nums[i] === 0) {
      answer.push(pq.shift() || 0);
    } else {
      pq.insert(nums[i]);
    }
  }

  return answer.join("\n");
}

console.log(solution(N, NUMS));