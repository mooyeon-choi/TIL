function solution(n) {
  return Math.sqrt(n) % 1 ? -1 : (Math.sqrt(n) + 1) ** 2;
}
