t = int(input())
for tc in range(1, t + 1):
    word = input()
    result_list = []
    result = []
    answer = 1
    for string in word:
        if string in '{}()':
            result_list.append(string)
    if len(result_list) % 2:
        answer = 0
        print('#{} {}'.format(tc, answer))
    else:
        result.append(result_list.pop())
        for i in range(len(result_list)):
            if result[-1] == ')' and result_list[-1] == '(':
                result.pop()
                result_list.pop()
            elif result[-1] == '}' and result_list[-1] == '{':
                result.pop()
                result_list.pop()
            elif result[-1] == ')' and len(result_list):
                result.append(result_list.pop())
            elif result[-1] == '}' and len(result_list):
                result.append(result_list.pop())
            else:
                answer = 0
                break
        print('#{} {}'.format(tc, answer))