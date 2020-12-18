def solution(k, room_number):
    answer = []
    num_dict = {}
    def find(n):
        n_list = []
        while True:
            if n in num_dict:
                n_list.append(n)
                n = num_dict[n]
            else:
                for nums in n_list:
                    num_dict[nums] = n + 1
                num_dict[n] = n + 1
                return n
    for number in room_number:
        answer.append(find(number))
    return answer