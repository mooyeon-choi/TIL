class Solution {
    public String solution(String s) {
        String answer = "";
        int center = (int) s.length() / 2;
        if (s.length() % 2 == 1) {
            answer = s.substring(center, center + 1);
        } else {
            answer = s.substring(center - 1, center + 1);
        }
        return answer;
    }
}

// 더 간단한 방법
class Solution {
    public String solution(String s) {
        return s.substring((s.length() - 1) / 2, s.length() / 2 + 1);
    }
}