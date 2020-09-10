def quick_sort(lo, hi):
    if lo >= hi:
        return
    i, j = lo, hi
    while i < j:
        while i < n and numbers[i] <= numbers[lo]:
            i += 1
        while numbers[j] > numbers[lo]:
            j -= 1
        if i >= j: break
        numbers[i], numbers[j] = numbers[j], numbers[i]
    numbers[j], numbers[lo] = numbers[lo], numbers[j]

    quick_sort(lo, j - 1)
    quick_sort(j + 1, hi)


t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    numbers = list(map(int, input().split()))
    quick_sort(0, len(numbers) - 1)
    print('#{} {}'.format(tc, numbers[len(numbers)//2]))