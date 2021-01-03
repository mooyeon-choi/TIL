function solution(a, b) {
  const days = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"];
  const months = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30];
  return days[(months.slice(0, a).reduce((x, y) => x + y, 0) + b) % 7];
}
