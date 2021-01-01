function solution(n) {
  let number = "";
  let answer = 0;
  while (n > 0) {
    number = (n % 3) + number;
    n = Math.floor(n / 3);
  }
  for (let i = 0; i < number.length; i++) {
    answer += number[i] * 3 ** i;
  }
  return answer;
}

// 다른 사람 풀이
const solution = (n) => {
  return parseInt([...n.toString(3)].reverse().join(""), 3);
};
