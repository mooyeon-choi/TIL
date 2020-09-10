n = int(input())
n_list = list(map(str, input().split()))
m = int(input())
m_list = list(map(str, input().split()))
result = ['0'] * m

n_list.sort()
for i in range(m):
    left = 0
    right = n - 1
    while left <= right:
        point = int((left + right) / 2)
        if n_list[point] > m_list[i]:
            right = point - 1
        elif n_list[point] < m_list[i]:
            left = point + 1
        if n_list[point] == m_list[i]:
            result[i] = '1'
            break

print('{}'.format(' '.join(result)))
