def back(left, right, strings):
    if left == n:
        result.add(strings + ')'*(n-right))
    else:
        if left > right:
            back(left, right + 1, strings + ')')
        back(left + 1, right, strings + '(')
        

result = set()
n = 0
def solution(_):
    global n
    n = _
    back(0, 0, '')
    return len(result)