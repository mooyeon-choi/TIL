function solution(arr) {
  const minNum = Math.min(...arr);
  return arr.length > 1 ? arr.filter((num) => num !== minNum) : [-1];
}

// 다른 사람의 풀이 lsw015 , developer-do , 노국현 , - , 정만수님 외 9 명
function solution(arr) {
  arr.splice(arr.indexOf(Math.min(...arr)), 1);
  return arr.length > 0 ? arr : [-1];
}
