function Queue() {
    this.items = [];
    this.head = 0;
  }
  
  Queue.prototype.enqueue = function(item) {
    this.items.push(item);
  };
  
  Queue.prototype.dequeue = function() {
    if (this.isEmpty()) return undefined;
    const value = this.items[this.head];
    this.head += 1;

    if (this.head > 1000) {
      this.items = this.items.slice(this.head);
      this.head = 0;
    }

    return value;
  };
  
  Queue.prototype.peek = function() {
    return this.items[this.head];
  };
  
  Queue.prototype.isEmpty = function() {
    return this.items.length === this.head;
  };
  
  // 사용 예시
  const queue = new Queue();
  queue.enqueue(1);
  queue.enqueue(2);
  queue.enqueue(3);
  
  console.log(queue.dequeue()); // 1