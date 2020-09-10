T = int(input())

for word in range(T):
    torf = 0
    test = input()
    for i in range(len(test)//2):
        if test[i] != test[-i-1]:
            torf = 0
            break
    else:
        torf = 1
    print(f'#{word+1} {torf}')