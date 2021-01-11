function solution(nums) {
  const answer = new Set(nums);
  return answer.size <= nums.length / 2 ? answer.size : nums.length / 2;
}
