function solution(arr1, arr2) {
  return arr1.map((arr, i) => arr.map((a, j) => a + arr2[i][j]));
}
