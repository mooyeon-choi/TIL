function solution(x, n) {
  let answer = [];
  for (let i = x; i <= n; i += x) {
    answer.push(x * i);
  }
  return answer;
}

// 다른 사람의 풀이
// Hyunyoung Cho , 김재균 , 김성훈 , - , 김선수 외 15 명
// 정형석 , 장유현 , 김성백 님의 풀이를 조금 변형함
function solution(x, n) {
  return [...Array(n)].map((v, idx) => (idx + 1) * x);
}
