// const input = require("fs")
//   .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
//   .toString()
//   .trim()
//   .split("\n");

const input = `3 2
1 65
5 23
2 99
10
2`
  .split("\n");

const [N, K] = input[0].split(" ").map(Number);
const jewels = input.slice(1, 1 + N).map(arr => arr.split(" ").map(Number));
const bags = input.slice(1 + N).map(Number).sort((a, b) => a - b);

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
      if (childIndex > size || compare(heap[pos * 2][0], heap[childIndex][0]) < 0)
        childIndex = pos * 2;
      const child = heap[childIndex];
      if (compare(item[0], child[0]) <= 0)
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
      if (compare(parent[0], item[0]) <= 0)
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

function solution() {
  const pq = new PriorityQueue((a, b) => a[0] - b[0]);

  let answer = 0;
  let memo = 0;
  for (let i = 0; i < K; i++) {
    let j = 0;
    while (j < N && jewels[j][0] <= bags[i]) {
      pq.insert(jewels[j]);
      j++;
    }

    let num = 0;
    while (pq.peek() !== undefined) {
      if (pq.peek()[0] <= bags[i]) {
        if (pq.peek()[1] > num) {
            memo = Math.max(memo, num);
            num = pq.peek()[1];
        }
        pq.shift();
      } else {
        break;
      }
    }

    answer += Math.max(memo, num);
  }

  return answer;
}

console.log(solution());
