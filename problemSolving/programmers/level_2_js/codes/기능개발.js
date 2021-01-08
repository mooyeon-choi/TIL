function solution(progresses, speeds) {
    const answer = [];
    let time = 1;
    let cnt = 0;
    for (let i = 0; i < progresses.length; i++) {
        if (progresses[i] + speeds[i] * time < 100) {
            i !== 0 && answer.push(cnt)
            time = Math.ceil((100 - progresses[i]) / speeds[i]);
            cnt = 1
        } else {
            cnt += 1
        }
    }
    answer.push(cnt)
    return answer;
}