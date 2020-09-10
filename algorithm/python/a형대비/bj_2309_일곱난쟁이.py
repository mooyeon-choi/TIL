def back():
    for i in range(1 << 9):
        result = []
        for j in range(9):
            if i & (1 << j):
                result.append(num_list[j])
        if sum(result) == 100 and len(result) == 7:
            return result

used = [0]*9
num_list = []
for _ in range(9):
    num_list.append(int(input()))
answer = back()
answer.sort()
for num in answer:
    print(num)