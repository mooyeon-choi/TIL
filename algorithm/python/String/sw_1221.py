t = int(input())
for tc in range(1, t + 1):
    numbers = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    test, number = map(str, input().split())
    num_list = list(map(str, input().split()))
    result = []
    count = 0
    for i in range(10):
        for j in num_list:
            if j == numbers[count]:
                result.append(j)
        count += 1
    print('#{}\n{}'.format(tc, ' '.join(result)))