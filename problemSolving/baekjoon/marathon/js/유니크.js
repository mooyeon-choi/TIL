const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n")
  .map((el) => el.split(" ").map(Number));

const [N] = input[0];
const users = input.slice(1);

const answer = new Array(users.length).fill(0);

function game(n, users, answer) {
    for (let i = 0; i < 3; i++) {
        for (let j = 0; j < n; j++) {
            let check = false;
            for (let k = 0; k < n; k++) {
                if (j !== k && users[j][i] === users[k][i]) check = true;
            }
            if (!check) answer[j] += users[j][i];
        }
    }

    return answer;
}

console.log(game(N, users, answer).join("\n"));