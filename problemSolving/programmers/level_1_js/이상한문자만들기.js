function solution(s) {
  var answer = [];
  let cnt = 0;
  for (let i = 0; i < s.length; i++) {
    if (s[i] !== " ") {
      if (cnt === 0) {
        answer.push(s[i].toUpperCase());
        cnt = 1;
      } else {
        answer.push(s[i].toLowerCase());
        cnt = 0;
      }
    } else {
      answer.push(s[i]);
      cnt = 0;
    }
  }
  return answer.join("");
}

// 다른 사람의 풀이 탈퇴한 사람의 풀이
function solution(s) {
  function change(a) {
    return a[0].toUpperCase() + a[1].toLowerCase();
  }
  return s.toUpperCase().replace(/(\w)(\w)/g, change);
}

// ._.님의 풀이
function solution(s) {
  return s
    .split(" ")
    .map((a) => {
      return a
        .split("")
        .map((b, i) => {
          return i % 2 === 0 ? b.toUpperCase() : b.toLowerCase();
        })
        .join("");
    })
    .join(" ");
}
