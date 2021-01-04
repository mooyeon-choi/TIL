function solution(num) {
  for (let i = 0; i < 501; i++) {
      if (num === 1) {
          return i
      } else {
          num & 1 ? num = num * 3 + 1 : num /= 2;
      }
  }
  return -1;
}