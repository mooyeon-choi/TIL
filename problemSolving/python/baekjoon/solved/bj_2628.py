w, h = map(int, input().split())
t = int(input())
cut_list = [[0], [0]]
for tc in range(t):
    cr, cn = map(int, input().split())
    cut_list[cr].append(cn)
cut_list[0].append(h)
cut_list[1].append(w)
past = 0
w_list = []
h_list = []
for r in sorted(cut_list[0]):
    if r == 0:
        past = 0
    else:
        w_list.append(r - past)
        past = r

for r in sorted(cut_list[1]):
    if r == 0:
        past = 0
    else:
        h_list.append(r - past)
        past = r
print(w_list, h_list)
max_num = 0
for i in w_list:
    for j in h_list:
        if i * j > max_num:
            max_num = i * j
print(max_num)