function solution(board, moves) {
  var answer = 0;
  var basket = new Array();
  for (var i in moves) {
    for (var j = 0; j < board.length; j++) {
      if (board[j][moves[i] - 1]) {
        if (basket.length > 0) {
          if (basket[basket.length - 1] === board[j][moves[i] - 1]) {
            answer += 2;
            board[j][moves[i] - 1] = 0;
            basket.pop();
            break;
          }
        }
        basket.push(board[j][moves[i] - 1]);
        board[j][moves[i] - 1] = 0;
        break;
      }
    }
  }
  return answer;
}
