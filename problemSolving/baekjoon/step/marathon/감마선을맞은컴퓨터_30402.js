const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString();

const pixel = input.replace(/[\n ]/g, "");

function solution(pixel) {
  for (let i = 0; i < pixel.length; i++) {
    if (pixel[i] === "w") {
      return "chunbae";
    }
    if (pixel[i] === "b") {
      return "nabi";
    }
    if (pixel[i] === "g") {
      return "yeongcheol";
    }
  }
  return "none";
}

console.log(solution(pixel));