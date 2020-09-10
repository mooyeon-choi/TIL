t = int(input())
for tc in range(1, t + 1):
    answer = 0xffffff
    n, b = map(int, input().split())
    persons = list(map(int, input().split()))
    for i in range(1 << n):
        member = []
        for j in range(n):
            if i & (1 << j):
                member.append(persons[j])
        num = sum(member) - b
        if num >= 0:
            if num < answer:
                answer = num
    print('#{} {}'.format(tc, answer))