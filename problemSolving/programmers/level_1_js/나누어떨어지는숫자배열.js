function solution(arr, divisor) {
  const result = arr.filter((num) => num % divisor == 0);
  return result.length > 0 ? result.sort((x, y) => x - y) : [-1];
}
