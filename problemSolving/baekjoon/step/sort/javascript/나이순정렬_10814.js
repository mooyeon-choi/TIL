const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n");

const N = Number(input[0]);
const members = input.slice(1, N + 1).map(line => {
    const [age, name] = line.split(" ");
    return { age: Number(age), name };
  });

function merge(left, right) {
  const result = [];
  let i = 0;
  let j = 0;

  while (i < left.length && j < right.length) {
    if (left[i].age <= right[j].age) {
      result.push(left[i]);
      i++;
    } else {
      result.push(right[j]);
      j++;
    } 
  }

  return [...result, ...left.slice(i), ...right.slice(j)];
}

function mergeSort(members) {
  if (members.length <= 1) return members;
  const mid = Math.floor(members.length / 2);
  return merge(mergeSort(members.slice(0, mid)), mergeSort(members.slice(mid)));
}

console.log(mergeSort(members).map(member => `${member.age} ${member.name}`).join("\n"));