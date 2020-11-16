import java.util.HashMap;

class Solution {
    public String solution(String[] participant, String[] completion) {
        HashMap<String, Integer> people = new HashMap<>();
        for (int i = 0; i < participant.length; i++) {
            people.put(participant[i], people.getOrDefault(participant[i], 0) + 1);
        }
        for (int i = 0; i < completion.length; i++) {
            int value = people.get(completion[i]);
            if (value > 1) {
                people.put(completion[i], value - 1);
            } else {
                people.remove(completion[i]);
            }
        }
        String answer = people.keySet().iterator().next();
        return answer;
    }
}