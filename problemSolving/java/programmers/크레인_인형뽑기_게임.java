import java.util.ArrayList;

class Solution {
    public int solution(int[][] board, int[] moves) {
        ArrayList<Integer> list = new ArrayList<Integer>();
        int answer = 0;
        for (int i = 0; i < moves.length; i++) {
            int now = moves[i] - 1;
            int num = 0;
            for (int j = 0; j < board.length; j++) {
                if (board[j][now] > 0) {
                    num = board[j][now];
                    board[j][now] = 0;
                    break;
                }
            }
            if (num > 0) {
                if (list.size() > 0) {
                    if (list.get(list.size() - 1) == num) {
                        answer += 2;
                        list.remove(list.size() - 1);
                    } else {
                        list.add(num);
                    }
                } else {
                    list.add(num);
                }
            }
        }
        return answer;
    }
}