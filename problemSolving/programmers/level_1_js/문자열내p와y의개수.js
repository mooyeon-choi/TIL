function solution(s) {
  let cntP = 0;
  let cntY = 0;
  for (let i = 0; i < s.length; i++) {
    if ((s[i] === "p") | (s[i] === "P")) cntP++;
    else if ((s[i] === "y") | (s[i] === "Y")) cntY++;
  }
  return cntP == cntY ? true : false;
}

// 다른 사람의 풀이 temp , - , - , - , - 외 23 명
function solution(s) {
  return s.match(/p/gi).length == s.match(/y/gi).length;
}
