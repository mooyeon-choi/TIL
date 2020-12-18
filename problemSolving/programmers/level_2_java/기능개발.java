import java.util.ArrayList;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        ArrayList<Integer> answer = new ArrayList<Integer>();
        int memo = (100 - progresses[0]) / speeds[0];
        if ((100 - progresses[0]) % speeds[0] > 0)
            memo += 1;
        int cnt = 1;
        for (int i = 1; i < progresses.length; i++) {
            int now = (100 - progresses[i]) / speeds[i];
            if ((100 - progresses[i]) % speeds[i] > 0)
                now += 1;
            if (now <= memo) {
                cnt += 1;
            } else {
                answer.add(cnt);
                memo = now;
                cnt = 1;
            }
        }
        answer.add(cnt);
        return answer.stream().mapToInt(i -> i).toArray();
    }
}