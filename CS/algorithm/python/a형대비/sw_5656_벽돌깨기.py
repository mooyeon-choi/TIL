for tc in range(1, int(input()) + 1):
    n, w, h = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(h)]
    for i in range(h):
        print(board[i])