const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const N = Number(input[0]);
const arr = input.slice(1);

function solution(n, arr) {
  const answer = [];

  for (let i = 0; i < n; i++) {
    const numList = arr[i].split('');
    const numSet = new Set(numList);
    
    answer.push(numSet.size);
  }
  return answer.join('\n');
}

console.log(solution(N, arr));