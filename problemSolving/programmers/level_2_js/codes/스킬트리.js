function solution(skill, skill_trees) {
  var answer = 0;
  let before;
  let check;
  for (let i = 0; i < skill_trees.length; i++) {
      before = -1;
      check = true;
      for (let j = 0; j < skill.length; j++) {
          if (skill_trees[i].indexOf(skill[j]) !== -1) {
              if (skill_trees[i].indexOf(skill[j]) > before) {
                  before = skill_trees[i].indexOf(skill[j]);
              } else {
                  check = false;
                  break;
              }
          } else {
              before = 27;
          }
      }
      answer += check ? 1 : 0
  }
  return answer;
}

// 다른 사람의 풀이 iRequestUResponse , milliwonaire , 박하영님의 풀이
function solution(skill, skill_trees) {
  function isCorrect(n) {
      let test = skill.split('');
      for (var i = 0; i < n.length; i++) {
          if (!skill.includes(n[i])) continue;
          if (n[i] === test.shift()) continue;
          return false;
      }
      return true;
  }    

  return skill_trees.filter(isCorrect).length;
}