function solution(citations) {
  citations.sort((x, y) => y - x);
  for (let i = 0; i < citations.length; i++) {
      if (citations[i] < i + 1) {
          return i;
      }
  }
  return citations.length;
}