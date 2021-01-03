function solution(arr) {
  const answer = [];
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] != arr[i - 1]) {
      answer.push(arr[i]);
    }
  }
  return answer;
}

// 다른 사람의 풀이 jungting20 , - , 탈퇴한 사용자 , - , Junpil Hwang 외 116 명
function solution(arr) {
  return arr.filter((val, index) => val != arr[index + 1]);
}
