const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n");

const [C, N] = input[0].split(" ").map(Number);
const chickens = input.slice(1, C + 1).map(Number);
const cows = input.slice(C + 1).map((item) => item.split(" ").map(Number));

chickens.sort((a, b) => a - b);
cows.sort((a, b) => a[0] - b[0]);

function solution() {
  let answer = 0;
  let cowIdx = 0;
  const memo = new Array(N).fill(false);

  for (let i = 0; i < C; i++) {
    const chickenTime = chickens[i];
    
    while (cowIdx < N && cows[cowIdx][0] <= chickenTime) {
      cowIdx++;
    }
    
    let bestCow = -1;
    let minEnd = Infinity;
    
    for (let j = 0; j < cowIdx; j++) {
      if (!memo[j] && cows[j][0] <= chickenTime && cows[j][1] >= chickenTime) {
        if (cows[j][1] < minEnd) {
          minEnd = cows[j][1];
          bestCow = j;
        }
      }
    }
    
    if (bestCow !== -1) {
      memo[bestCow] = true;
      answer++;
    }
  }
  
  return answer;
}

console.log(solution());