function solution(s) {
  const number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"];
  if ((s.length !== 4) & (s.length !== 6)) {
    return false;
  }
  for (let i = 0; i < s.length; i++) {
    if (!(s[i] in number)) {
      return false;
    }
  }
  return true;
}

// 다른 사람의 풀이
function alpha_string46(s) {
  var regex = /^\d{6}$|^\d{4}$/;
  return regex.test(s);
}
