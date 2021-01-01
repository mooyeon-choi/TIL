function solution(strings, n) {
  return strings.sort((x, y) => {
      return x[n] > y[n] ? 1 : x[n] === y[n] ? x > y ? 1 : -1
  });
}

// 다른 사람의 풀이
function solution(strings, n) {
  return strings.sort((s1, s2) => s1[n] === s2[n] ? s1.localeCompare(s2) : s1[n].localeCompare(s2[n]));
}