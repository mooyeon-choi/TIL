const input = `3
2 3
2 2 2
3 3 1
2 3
1 3 2
1 3 1
5 5
5 5 1
4 4 2
3 3 3
2 2 4
1 1 5`
  .split("\n");

const T = Number(input[0]);
const testCases = input.slice(1);

function solution(index, n, k, arr) {
  const dp = arr.map(row => row.split(" ").map(BigInt)).sort((a, b) => a[1] - b[1]);

  console.log(`Case #${index}: ${answer}`);
}

let idx = 0;

for (let i = 1; i <= T; i++) {
  const [n, k] = testCases[idx].split(" ").map(Number);
  const arr = [];

  for (let j = 0; j < n; j++) {
    arr.push(testCases[idx + 1 + j]);
  }

  solution(i, n, k, arr);

  idx += 1 + n;
}
