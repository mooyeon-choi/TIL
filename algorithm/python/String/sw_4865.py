t = int(input())
for tc in range(1, t + 1):
    word = input()
    random_word = input()
    word_dict = {}
    max_num = 0
    for key in word:
        word_dict[key] = 0
    for string in random_word:
        if string in word_dict:
            word_dict[string] += 1
    for value in word_dict.values():
        if value > max_num:
            max_num = value
    print('#{} {}'.format(tc, max_num))