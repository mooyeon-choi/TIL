function solution(participant, completion) {
  const result = {};
  for (let i = 0; i < participant.length; i++) {
    if (!(participant[i] in result)) {
      result[participant[i]] = 0;
    } else {
      result[participant[i]] += 1;
    }
  }
  for (let i = 0; i < completion.length; i++) {
    if (result[completion[i]] === 0) {
      delete result[completion[i]];
    } else {
      result[completion[i]] -= 1;
    }
  }
  return Object.keys(result)[0];
}

// 다른 사람의 풀이(최인규 , 서경우 , 최민수 , charles2 님의 풀이)
var solution = (participant, completion) =>
  participant.find(
    (name) => !completion[name]--,
    completion.map((name) => (completion[name] = (completion[name] | 0) + 1))
  );
