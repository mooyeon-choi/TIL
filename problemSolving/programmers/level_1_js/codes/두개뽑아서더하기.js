function solution(numbers) {
  var answer = [];
  numbers.sort();
  for (let i = 0; i < numbers.length; i++) {
    for (let j = i + 1; j < numbers.length; j++) {
      if (
        answer.find((item) => item === numbers[i] + numbers[j]) === undefined
      ) {
        answer.push(numbers[i] + numbers[j]);
      }
    }
  }
  answer.sort((a, b) => a - b);
  return answer;
}
