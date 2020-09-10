def subset():
    for i in range(1 << c):
        word = ''
        for j in range(c):
            if i & (1<<j):
                word += words[j]
        if len(word) == l:
            count1, count2 = 0, 0
            for w in word:
                if w in 'aeiou':
                    count1 += 1
                else:
                    count2 += 1
            if count1 > 0 and count2 > 1:
                result.append(word)


l, c = map(int, input().split())
words = list(map(str, input().split()))
words.sort()
result = []
subset()
result.sort()
for word in result:
    print(word)