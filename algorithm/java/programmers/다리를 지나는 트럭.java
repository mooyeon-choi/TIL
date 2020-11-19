class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int answer = 0;
        int[] visit = new int[truck_weights.length];
        int left = 0;
        int right = 0;
        int total_weight = 0;
        while (left < truck_weights.length) {
            if (right < truck_weights.length) {
                if (total_weight + truck_weights[right] <= weight) {
                    answer += 1;
                    visit[right] = answer;
                    total_weight += truck_weights[right];
                    right += 1;
                } else if (left < right) {
                    if (answer < visit[left] + bridge_length)
                        answer = visit[left] + bridge_length - 1;
                    total_weight -= truck_weights[left];
                    left += 1;
                }
            } else {
                answer = visit[left] + bridge_length;
                total_weight -= truck_weights[left];
                left += 1;
            }
        }
        return answer;
    }
}