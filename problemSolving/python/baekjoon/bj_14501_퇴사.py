def back(num, c_list, p_list):
    if not c_list:
        result.append(num)
        return
    else:
        for i in range(len(c_list)):
            if c_list[i] <= len(c_list) - i:
                back(num + p_list[i], c_list[c_list[i]+i:], p_list[c_list[i]+i:])
        else:
            result.append(num)
            return
    return

n = int(input())
t = []
p = []
result = []
for _ in range(n):
    tn, pn = map(int, input().split())
    t.append(tn)
    p.append(pn)
back(0, t, p)
print(max(result))