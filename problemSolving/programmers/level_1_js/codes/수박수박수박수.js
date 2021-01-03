function solution(n) {
  var answer = "";
  for (let i = 0; i < n; i++) {
    if (i & 1) {
      answer += "박";
    } else {
      answer += "수";
    }
  }
  return answer;
}

// 다른 사람의 풀이 이수관 님의 풀이
const waterMelon = (n) => {
  return "수박".repeat(n / 2) + (n % 2 === 1 ? "수" : "");
};
