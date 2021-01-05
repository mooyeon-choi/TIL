function solution(phone_number) {
  return phone_number
    .split("")
    .reduce((x, y, idx) => (x += idx < phone_number.length - 4 ? "*" : y), "");
}

function solution(phone_number) {
  return phone_number
    .split("")
    .map((num, idx) => (idx < phone_number.length - 4 ? "*" : num))
    .join("");
}
