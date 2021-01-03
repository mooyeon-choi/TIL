function solution(a, b) {
  return a > b ? ((a + b) * (a - b + 1)) / 2 : ((a + b) * (b - a + 1)) / 2;
}

// 다른 사람의 풀이 박홍철 님의 풀이
function adder(a, b) {
  return ((a + b) * (Math.abs(b - a) + 1)) / 2;
}
