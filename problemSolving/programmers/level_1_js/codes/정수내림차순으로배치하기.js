function solution(n) {
  return parseInt(
    n
      .toString()
      .split("")
      .sort((x, y) => parseInt(y) - parseInt(x))
      .join("")
  );
}
