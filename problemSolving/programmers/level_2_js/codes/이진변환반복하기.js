function solution(s) {
  const answer = [0, 0];
  while (s.length > 1) {
    answer[0]++;
    answer[1] += s.match(/[0]/g) ? s.match(/[0]/g).length : 0;
    s = s.split("0").join("").length.toString(2);
  }
  return answer;
}
