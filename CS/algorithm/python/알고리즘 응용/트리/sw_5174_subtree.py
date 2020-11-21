def inorder(v):
    global answer
    if not v: return
    answer += 1
    inorder(L[v])
    inorder(R[v])
    if v == N: return



t = int(input())
for tc in range(1, t + 1):
    answer = 0
    E, N = map(int, input().split())
    L = [0]*(E+2)
    R = [0]*(E+2)
    nums = list(map(int, input().split()))
    for i in range(0, len(nums), 2):
        if not L[nums[i]]:
            L[nums[i]] = nums[i+1]
        else:
            R[nums[i]] = nums[i+1]
    inorder(N)
    print('#{} {}'.format(tc, answer))