function solution(n) {
  const cnt = n.toString(2).match(/[1]/g).length;
  while (true) {
    n++;
    if (n.toString(2).match(/[1]/g).length === cnt) {
      return n;
    }
  }
}
