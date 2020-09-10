A = ['co', 'dil', 'ity']
def back(word_list, word_sum):
    global answer
    if len(word_sum) > answer:
        answer = len(word_list)
    for i in range(len(word_list)):
        if not used[i]:
            if len(word_list[i] + word_sum) == len(word_list[i]) + len(word_sum):
                used[i] = 1
                back(word_list, word_list[i] + word_sum)
                used[i] = 0

answer = 0
used = []
def Solution(A):
    can = []
    for word in A:
        a = set(word)
        if len(word) == len(a):
            can.append(a)
    used = [0]*len(can)
    back(can, set())

Solution(A)
print(answer)