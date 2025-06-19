const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

let index = 0;
const songs = [];

while (index < input.length - 1) {
  const N = Number(input[index]);

  songs.push(input.slice(index + 1, index + N + 1));

  index += N + 1;
}

function solution(songs) {
  const answer = [];

  for (let i = 0; i < songs.length; i++) {
    answer.push(`${i + 1}`);
    const sortedSongs = [...songs[i]].sort((a, b) => a.localeCompare(b));
    answer.push(sortedSongs.join('\n'));
  }

  return answer.join('\n');
}

console.log(solution(songs));
