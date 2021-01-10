function solution(brown, yellow) {
  for (let i = (brown + 4) / 2 - 3; i >= (brown + 4) / 4; i--) {
    if (i * ((brown + 4) / 2 - i) === brown + yellow) {
      return [i, (brown + 4) / 2 - i];
    }
  }
}
