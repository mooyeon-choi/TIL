function solution(n, t, m, p) {
  const result = [];
  let answer = "";
  let num = 0;
  while (result.length < t * m) {
    result.push(...num.toString(n).toUpperCase().split(""));
    num++;
  }
  for (let i = p - 1; i < result.length; i += m) {
    answer += result[i];
    if (answer.length === t) break;
  }
  return answer;
}
