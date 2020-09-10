def makeOrder(numbers):
    if len(numbers) >= 9:
        order.append(numbers)
    for i in range(1, 10):
        if i not in numbers:
            makeOrder(numbers+[i])

n = int(input())
taja = [list(map(int, input().split())) for _ in range(n)]
order = []
makeOrder([])
for i in range(len(order)):
    print(order[i])