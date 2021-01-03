function solution(n) {
  return n
    .toString()
    .split("")
    .reduce((x, y) => (x += parseInt(y)), 0);
}
