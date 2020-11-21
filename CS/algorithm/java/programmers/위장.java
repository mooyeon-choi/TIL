import java.util.HashMap;

class Solution {
    public int solution(String[][] clothes) {
        HashMap<String, Integer> clothMap = new HashMap<>();
        for (int i = 0; i < clothes.length; i++) {
            clothMap.put(clothes[i][1], clothMap.getOrDefault(clothes[i][1], 1) + 1);
        }
        int answer = 1;;
        Integer[] clothNums = clothMap.values().toArray(new Integer[0]);
        for (int i = 0; i < clothNums.length; i++) {
            answer *= clothNums[i];
        }
        
        return answer - 1;
    }
}