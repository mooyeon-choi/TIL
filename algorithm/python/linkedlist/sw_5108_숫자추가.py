def insertAt(idx, node):  # idx: 삽입 위치, node: 삽입 노드
    cur, prev = node, numbers[idx]
    while idx < len(numbers):
        prev = numbers[idx]
        numbers[idx] = cur
        cur = prev
        idx += 1
    numbers.append(cur)


t = int(input())
for tc in range(1, t + 1):
    n, m, l = map(int, input().split())
    numbers = list(map(int, input().split()))
    for _ in range(m):
        i, j = map(int, input().split())
        insertAt(i, j)
    print('#{} {}'.format(tc, numbers[l]))