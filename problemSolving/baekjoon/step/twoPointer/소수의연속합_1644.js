const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim();

const N = Number(input);

function findPrimes(num) {
  let arr = Array(N + 1).fill(true).fill(false, 0, 2);
    for(let i = 2 ; i * i <= N; i++){
        if(arr[i]){
            for(let j = i * i; j <= N; j+=i){
                arr[j] = false;
            }
        }
    }

    return arr;
}

function solution() {
  const primes = findPrimes(N);
  let answer = 0;
  let left = 0;
  let right = 0;
  let sum = 0;

  while (right < primes.length) {
    if (primes[right]) {
      sum += right;
    }

    while (sum > N && left < right) {
      if (primes[left]) {
        sum -= left;
      }
      left++;
    }

    if (sum === N && primes[right]) {
      answer++;
    }

    right++;
  }

  return answer;
}

console.log(solution());