# C-style
S = [0] * 3
top = -1

def push(item):
    global top
    # full-상태에 주의 if top == 마지막 인덱스:
    top += 1
    S[top] = item

def pop():
    # empty-상태를 체크