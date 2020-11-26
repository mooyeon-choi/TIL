def dfs(i, j, string):
    string += board[i][j]
    if len(string) == 7:
        result.add(string)
        return
    if 0 <= i - 1:
        dfs(i - 1, j, string)
    if i + 1 < 4:
        dfs(i + 1, j, string)
    if 0 <= j - 1:
        dfs(i, j - 1, string)
    if j + 1 < 4:
        dfs(i, j + 1, string)


for tc in range(1, int(input()) + 1):
    result = set()
    board = [input().split() for _ in range(4)]
    for i in range(4):
        for j in range(4):
            dfs(i, j, '')
    print('#{} {}'.format(tc, len(result)))
