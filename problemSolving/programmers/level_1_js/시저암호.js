function solution(s, n) {
  const answer = [];
  for (let i = 0; i < s.length; i++) {
    if (s[i] !== " ") {
      const word = s.charCodeAt(i);
      if ((word >= 65) & (word <= 90)) {
        answer.push(
          String.fromCharCode(word + n > 90 ? word + n - 26 : word + n)
        );
      } else {
        answer.push(
          String.fromCharCode(word + n > 122 ? word + n - 26 : word + n)
        );
      }
    } else {
      answer.push(" ");
    }
  }
  return answer.join("");
}

// 다른 사람의 풀이 쿠키님의 풀이
function solution(s, n) {
  var upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
  var lower = "abcdefghijklmnopqrstuvwxyz";
  var answer = "";

  for (var i = 0; i < s.length; i++) {
    var text = s[i];
    if (text == " ") {
      answer += " ";
      continue;
    }
    var textArr = upper.includes(text) ? upper : lower;
    var index = textArr.indexOf(text) + n;
    if (index >= textArr.length) index -= textArr.length;
    answer += textArr[index];
  }
  return answer;
}
