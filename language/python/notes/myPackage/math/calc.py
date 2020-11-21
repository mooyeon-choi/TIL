def sum(a, b):
    """
    두 수를 더합니다
    """
    return a + b

def sub(a, b):
    """
    두 수를 뺍니다.
    """
    return a - b

def mul(a, b):
    """
    두 수를 곱합니다.
    """
    return a * b

def div(a, b):
    """
    두 수를 나눕니다.
    """
    if b == 0:
        return False
    return a / b